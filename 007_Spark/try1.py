from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import sql
from pyspark.sql import SQLContext
from pyspark.sql import types
import json
import csv
from json import loads
from flatten_json import flatten
from time import sleep
import pandas as pd

# spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 try1.py

sc = SparkContext(appName="samir")                                                                                     
ssc = StreamingContext(sc, 5)          

ks = KafkaUtils.createDirectStream(ssc, ['kafkaNBA2'], {'metadata.broker.list': 'localhost:9096'})   

# result1 = ks.map(lambda x: json.loads(x[1])).flatMap(lambda x: x['data']).map(lambda x: x['player']['weight_pounds'])


result1 = ks.map(lambda x: json.loads(x[1])).flatMap(lambda x: x['data']).map(lambda x: x['player'])

# result = ks.map(lambda x: json.loads(x[1])).flatMap(lambda x: x['data'])

result1.pprint()

def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global ss                                                                                                       
        df = ss.createDataFrame(rdd, schema=['first_name','last_name', 'height_inches', 'weight_pounds','team_id','height_feet','position','id'])                                                
        df.show()                                                                                                       
        df.write.saveAsTable(name='default.nba1', format='hive', mode='append')  


                                                                                           
ss = SparkSession.builder.appName("samir").config("spark.sql.warehouse.dir", "/user/hive/warehouse/").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()                                                                                                  
ss.sparkContext.setLogLevel('WARN') 
                                
result1.foreachRDD(handle_rdd) 


ssc.start()                                                                                                             
ssc.awaitTermination()