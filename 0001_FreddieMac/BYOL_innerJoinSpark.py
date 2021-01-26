from pyspark.sql import functions as F
from pyspark import SparkFiles
from pyspark.sql import SparkSession



spark = SparkSession.builder.appName('reads3bucket').getOrCreate()

s3_out_uri="s3://freddie-mac-sandbox-raw-plus/rimes/index/ftse_idx_std/parquet/BYOL/"

df_laus=spark.read.csv("s3://freddie-mac-sandbox-raw/rimes/index/ftse_idx_std/BYOL.100SalesRecords.csv")
df_laus.createOrReplaceTempView("input_laus")
df_borr=spark.read.csv("s3://freddie-mac-sandbox-raw/rimes/index/ftse_idx_std/BYOL.5000SalesRecords.csv")
df_borr.createOrReplaceTempView("input_borr")

df_joined=spark.sql("""SELECT
                       a.region,
                       a.country,
                       a.itemTtype,
                       a.saleschannel,
                       a.orderpriority,
                       a.orderdate,
                       a.orderid,
                       a.shipdate,
                       a.unitssold,
                       a.unitprice,
                       a.unitcost,
                       a.totalrevenue,
                       a.totalcost,
                       a.totalprofit
                       FROM input_laus a JOIN input_borr b
                       ON a.itemtype = b.itemtype""")


df_inner_joined_final=df_joined.withColumn('dttm_lst_updt_lake', F.current_timestamp())

a=df_inner_joined_final.count()

print(f'Staging count is :{a}')

df_inner_joined_final.write.format("parquet").mode("overwrite").save(s3_out_uri)

df_read_s3=spark.read.parquet(s3_out_uri)

b=df_read_s3.count()

print(f'Final count is :{b}')