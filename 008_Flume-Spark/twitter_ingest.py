from pyspark.streaming import StreamingContext
from pyspark import SparkContext, SparkConf
from pyspark import sql
from pyspark.sql import SQLContext
from pyspark.sql import types
import json
import csv
from json import loads
from time import sleep
from pyspark.streaming.flume import FlumeUtils


sc =SparkContext()
ssc = StreamingContext(sc,5)
flumeStream = FlumeUtils.createStream(ssc, "localhost", 6669)
sqlContext = sql.SQLContext(sc)
sleep(3)
lines = flumeStream.map(lambda x: x[1])

print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")

def transformer(rdd):
    if not rdd.isEmpty():
        rdd.lower()
        rdd.split()
        return rdd
   
   
transform=lines.map(transformer)

def build_df(rdd):
    if not rdd.isEmpty():
         global sqlc
         return (len(rdd))
         df=sqlc.createDataFrame(rdd,shema=['Time','Tweet','location'])
         df.show()
transform.foreachRDD(build_df)
transform.pprint()
 
ssc.start()
ssc.awaitTermination()