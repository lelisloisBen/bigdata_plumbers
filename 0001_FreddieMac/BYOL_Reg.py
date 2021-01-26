from pyspark.sql import functions as F
from pyspark import SparkFiles
from pyspark.sql import SparkSession

# Starting Spark Session
spark = SparkSession.builder.appName('firstDatasetBYOLregistration').getOrCreate()

# Path of the parquet file when it's transformed
s3_out_uri="s3://freddie-mac-sandbox-raw-plus/byol/parquet/"

# Reading the csv file from S3 raw Bucket 
df_sales100=spark.read.csv("s3://freddie-mac-sandbox-raw/byol/byol_sales_1.dataset.csv")

# Adding a Timestamp column for the parquet file
df_final=df_sales100.withColumn('edptimestamp', F.current_timestamp())

# counting row after adding Timestamps
a=df_final.count()

# Printing the count
print(f'Staging count is :{a}')

# Writing the parquet file to S3 raw-plus Bucket
df_final.write.format("parquet").mode("overwrite").save(s3_out_uri)

# Reading the parquet file after writing it
df_read_s3=spark.read.parquet(s3_out_uri)

# Counting the parquet file from row-plus Bucket
b=df_read_s3.count()

# Print Final count of parquet file
print(f'Final count is :{b}')