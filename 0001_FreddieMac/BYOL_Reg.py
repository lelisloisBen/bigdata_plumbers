from pyspark.sql import functions as F
from pyspark import SparkFiles
from pyspark.sql import SparkSession



spark = SparkSession.builder.appName('firstDatasetBYOLregistration').getOrCreate()

s3_out_uri="s3://freddie-mac-sandbox-raw-plus/byol/parquet/"

df_sales100=spark.read.csv("s3://freddie-mac-sandbox-raw/byol/byol_sales_1.dataset.csv")
# df_laus.createOrReplaceTempView("input_laus")

df_final=df_sales100.withColumn('edptimestamp', F.current_timestamp())

a=df_final.count()

print(f'Staging count is :{a}')

df_final.write.format("parquet").mode("overwrite").save(s3_out_uri)

df_read_s3=spark.read.parquet(s3_out_uri)

b=df_read_s3.count()

print(f'Final count is :{b}')