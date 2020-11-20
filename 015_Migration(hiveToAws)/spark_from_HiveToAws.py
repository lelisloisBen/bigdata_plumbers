from pyspark import SparkContext
from pyspark.sql import SparkSession, HiveContext

ss = SparkSession.builder\
        .master("local[1]")\
        .appName("QueryFromHive")\
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse/")\
        .config("hive.metastore.uris", "thrift://localhost:9083")\
        .enableHiveSupport()\
        .getOrCreate()

# AWS Access Key ID = AKIA4ESOEUICQDFJ4DKG
# AWS Secret key = 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


# ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
# ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3.awsAccessKeyId", "AKIA4ESOEUICVN3J4COL")
# ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3.awsSecretAccessKey", "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")
# ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3.enableServerSideEncryption", "true")
# ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3.serverSideEncryptionAlgorithm","AES256")



ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIA4ESOEUICQDFJ4DKG")
ss.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "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")


sqlContext = HiveContext(ss)

sqlContext.sql("use default")

sql = "SELECT * FROM nba1"

myDatas = sqlContext.sql(sql)


def myDataframe(df):
    df.show()
    df.write.mode('overwrite').parquet("s3a:///twitterkafkas3/test.parquet")
    # df.write.parquet("s3a:///twitterkafkas3/hive_nba1/test.parquet")
   
    
    # df.write.parquet("s3a:///twitterkafkas3/hive_nba1/test.parquet",mode="overwrite")



myDataframe(myDatas)


# dataFrame.write
# .format(“com.knoldus.spark.s3”)
# .option(“accessKey”,”s3_access_key”)
# .option(“secretKey”,”s3_secret_key”)
# .option(“bucket”,”bucket_name”)
# .option(“fileType”,”json”)
# .save(“sample.json”)

# import os
# import pyspark
# o
# s.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.10.34,org.apache.hadoop:hadoop-aws:2.7.2 pyspark-shell'
# from pyspark.sql import SQLContext
# from pyspark import SparkContext
# sc = SparkContext()
# sqlContext = SQLContext(sc)
# filePath = "s3a://yourBucket/yourFile.parquet"
# df = sqlContext.read.parquet(filePath) 