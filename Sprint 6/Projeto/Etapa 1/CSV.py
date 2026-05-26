import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, regexp_replace, trim
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_filmes_path = "s3://data-lake-yanmacedo/Raw/Local/CSV/Movies/"
input_series_path = "s3://data-lake-yanmacedo/Raw/Local/CSV/Series/"
output_filmes_path = "s3://data-lake-yanmacedo/Trusted/CSV/Parquet/Movies/"
output_series_path = "s3://data-lake-yanmacedo/Trusted/CSV/Parquet/Series/"

schema_filmes = StructType([
    StructField("id", IntegerType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", StringType(), True),
    StructField("numeroVotos", StringType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),
    StructField("anoFalecimento", StringType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

schema_series = StructType([
    StructField("id", IntegerType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("anoTermino", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", StringType(), True),
    StructField("numeroVotos", StringType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),
    StructField("anoFalecimento", StringType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

def process_data(input_path, output_path, schema):
    df = spark.read.csv(input_path, header=True, sep="|", nullValue='\\N', schema=schema)

    if "tituloPincipal" in df.columns:
        df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

    df = df \
        .withColumn("anoLancamento", regexp_replace(col("anoLancamento"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("tempoMinutos", regexp_replace(col("tempoMinutos"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("genero", trim(col("genero")).cast(StringType())) \
        .withColumn("notaMedia", regexp_replace(col("notaMedia"), "[^0-9.]", "").cast(FloatType())) \
        .withColumn("numeroVotos", regexp_replace(col("numeroVotos"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("anoNascimento", regexp_replace(col("anoNascimento"), "[^0-9]", "").cast(IntegerType())) \
        .withColumn("anoFalecimento", regexp_replace(col("anoFalecimento"), "[^0-9]", "").cast(IntegerType()))

    df.printSchema()

    df.write.mode("overwrite").parquet(output_path)

process_data(input_filmes_path, output_filmes_path, schema_filmes)
process_data(input_series_path, output_series_path, schema_series)

job.commit()