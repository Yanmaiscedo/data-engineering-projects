import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, lit, when, split, explode, floor

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


input_path_local = "s3://data-lake-yanmacedo/Trusted/Local/Parquet/Movies/2025/09/01/"
df_local = spark.read.parquet(input_path_local)

df_local_selected = df_local.select(
    col("id").cast("int"),
    col("tituloPrincipal"),
    col("tituloOriginal"),
    col("anoLancamento").cast("int"),
    col("genero"),
    col("notaMedia").cast("float"),
    col("numeroVotos").cast("int")
).withColumn("origem", lit("Local"))

df_local_filtered = df_local_selected.filter(
    (col("genero").rlike("(?i)Drama")) | (col("genero").rlike("(?i)Romance"))
)


input_path_tmdb = "s3://data-lake-yanmacedo/Trusted/TMDB/Parquet/2025/09/01/"
df_tmdb = spark.read.parquet(input_path_tmdb)

df_tmdb_selected = df_tmdb.select(
    col("id").cast("int"),
    col("tituloPrincipal"),
    col("tituloOriginal"),
    col("anoLancamento").cast("int"),
    col("genero"),
    col("notaMedia").cast("float"),
    col("numeroVotos").cast("int"),
    col("popularidade").cast("int")
).withColumn("origem", lit("TMDB"))


df_local_final = df_local_filtered.withColumn("popularidade", lit(None).cast("int"))
df_tmdb_final = df_tmdb_selected

df_union = df_local_final.unionByName(df_tmdb_final)

df_clean = df_union.dropDuplicates([
    "id", "tituloPrincipal", "tituloOriginal",
    "anoLancamento", "genero", "notaMedia", "numeroVotos", "origem"
])


dim_tempo = df_clean.select("anoLancamento") \
    .dropDuplicates() \
    .withColumnRenamed("anoLancamento", "ano") \
    .withColumn("decada", (floor(col("ano")/10)*10).cast("int")) \
    .withColumn("seculo", (floor(col("ano")/100)+1).cast("int"))

dim_genero = df_clean \
    .withColumn("genero_individual", explode(split(col("genero"), ","))) \
    .select(col("genero_individual").alias("genero")) \
    .dropDuplicates()

dim_avaliacao = df_clean.select("notaMedia").dropDuplicates().withColumn(
    "categoria",
    when(col("notaMedia") < 4, "Ruim")
    .when((col("notaMedia") >= 4) & (col("notaMedia") < 6), "Médio")
    .when((col("notaMedia") >= 6) & (col("notaMedia") < 8), "Bom")
    .when(col("notaMedia") >= 8, "Excelente")
)

dim_popularidade = df_clean.select("popularidade") \
    .dropna() \
    .dropDuplicates() \
    .withColumn("categoria",
        when(col("popularidade") < 100, "Baixa")
        .when((col("popularidade") >= 100) & (col("popularidade") < 500), "Média")
        .when((col("popularidade") >= 500) & (col("popularidade") < 1000), "Alta")
        .when(col("popularidade") >= 1000, "Muito Alta")
    )

dim_origem = df_clean.select("origem").dropDuplicates()


print("======= Fato Filmes =======")
df_clean.printSchema()
df_clean.show(5, truncate=False)

print("======= Dimensão Tempo =======")
dim_tempo.printSchema()
dim_tempo.show(5, truncate=False)

print("======= Dimensão Gênero =======")
dim_genero.printSchema()
dim_genero.show(5, truncate=False)

print("======= Dimensão Avaliação =======")
dim_avaliacao.printSchema()
dim_avaliacao.show(5, truncate=False)

print("======= Dimensão Popularidade =======")
dim_popularidade.printSchema()
dim_popularidade.show(5, truncate=False)

print("======= Dimensão Origem =======")
dim_origem.printSchema()
dim_origem.show(5, truncate=False)


output_base = "s3://data-lake-yanmacedo/Refined/"


df_clean.write.mode("overwrite").parquet(output_base + "Fato_Filmes/")

dim_tempo.write.mode("overwrite").parquet(output_base + "Dim_Tempo/")
dim_genero.write.mode("overwrite").parquet(output_base + "Dim_Genero/")
dim_avaliacao.write.mode("overwrite").parquet(output_base + "Dim_Avaliacao/")
dim_popularidade.write.mode("overwrite").parquet(output_base + "Dim_Popularidade/")
dim_origem.write.mode("overwrite").parquet(output_base + "Dim_Origem/")

job.commit()