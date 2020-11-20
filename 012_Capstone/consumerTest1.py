from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.sql import SparkSession
from collections import namedtuple 
import pyspark.sql.types as st 
import json
from json import loads
import math

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4,org.mongodb.spark:mongo-spark-connector_2.11:2.4.2 consumerTest1.py 

sc = SparkContext(appName="capstonePlayStore")                                                                                     
ssc = StreamingContext(sc, 10)    
# ss = SparkSession.builder.appName("capstonePlayStore").getOrCreate()                                                                                              
    


mymongo = SparkSession.builder.appName("capstonePlayStore")\
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/test.playstore") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/test.playstore") \
	.getOrCreate()

mymongo.sparkContext.setLogLevel('WARN') 

ks = KafkaUtils.createDirectStream(ssc, ['CapstoneSamirTest'], {'metadata.broker.list': 'localhost:9092'})   

result1 = ks.map(lambda x: json.loads(x[1]))

# res = result1.flatMap(lambda x: json.loads(x))

# res2 = res.map(lambda d: ( d['developerId'], d['title'],d['url'],d['priceText'], d['score'], ))

# test = result1.map(lambda d: d['developerId'], d['title'], d['url'], d['priceText'], d['score'] )
    

# res.pprint()

fields = ("developerId", "title", "url" , "priceText", "score", "scoreText" )
apps = namedtuple("applications", fields)

# myschema = st.StructType([
# 		st.StructField("developerId", st.StringType(), True),
# 		st.StructField("title", st.StringType(), True),
# 		st.StructField("url", st.StringType(), True ),
# 		st.StructField("priceText", st.StringType(), True),
# 		st.StructField("score", st.FloatType(), True),
#         st.StructField("scoreText", st.StringType(), True)
# 	])


def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global mymongo                                                                                 
        df = mymongo.createDataFrame(rdd)  
        # df.write.format("mongo").mode("append").save() 
        dfOrderdBy = df.orderBy('score', ascending=False)                               
        dfOrderdBy.show()
    	df.printSchema() 
                                                                                                   
         
data = result1.flatMap(lambda x: json.loads(x))\
    .map(lambda x: apps(x['developerId'], x['title'], x['url'], x['priceText'], x['score'], x['scoreText'] ))\
    .filter(lambda price: price[3] == 'FREE')\
    .filter(lambda numb: numb[4] > 4 )\
    .foreachRDD(lambda x: handle_rdd(x))

ssc.start()                                                                                                             
ssc.awaitTermination()