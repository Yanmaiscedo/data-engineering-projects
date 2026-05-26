import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, concat_ws
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, BooleanType, DateType, ArrayType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_file = "s3://data-lake-yanmacedo/Raw/TMDB/"
output_parquet = "s3://data-lake-yanmacedo/Trusted/JSON/Parquet/"

schema_filmes = StructType([
    StructField("id", IntegerType(), True),
    StructField("adult", BooleanType(), True),
    StructField("backdrop_path", StringType(), True),
    StructField("original_language", StringType(), True),
    StructField("original_title", StringType(), True),
    StructField("overview", StringType(), True),
    StructField("popularity", FloatType(), True),
    StructField("poster_path", StringType(), True),
    StructField("release_date", DateType(), True),
    StructField("title", StringType(), True),
    StructField("video", BooleanType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", IntegerType(), True),
    StructField("genre_ids", ArrayType(IntegerType()), True)
])

def process_data(input_path, output_path, schema):
    df = spark.read.option("multiLine", "true").schema(schema).json(input_path)
    df = df.withColumn("genre_ids", concat_ws(",", col("genre_ids")))
    df.printSchema()

    df.show(5, truncate=False)
    df.write.mode("overwrite").parquet(output_path)

process_data(input_file, output_parquet, schema_filmes)

job.commit()