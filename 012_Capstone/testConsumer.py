from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from collections import namedtuple 
import pyspark.sql.types as st 
from pyspark.sql import SparkSession

from pyspark.sql import SQLContext



sc = SparkContext(appName="PlayStore")                                                                                     
ssc = StreamingContext(sc, 10)   
sqlContext = SQLContext(sc)       

ks = KafkaUtils.createDirectStream(ssc, ['playstore'], {'metadata.broker.list': 'localhost:9092'})   

# result1 = ks.map(lambda x: json.loads(x[1]) )


# result1.pprint()

fields = ("developerId","title", "url" , "priceText", "score" )
apps = namedtuple("applications", fields)

myschema = st.StructType([
		st.StructField("developerId", st.IntegerType(), True),
		st.StructField("title", st.StringType(), True),
		st.StructField("url", st.StringType(), True ),
		st.StructField("priceText", st.StringType(), True),
		st.StructField("score", st.IntegerType(), True)
	])


def dataresults( rdd ):
    if not rdd.isEmpty():
    	df = sqlContext.createDataFrame(rdd, myschema)
    	df.show()
    	df.printSchema()


data = ks.map(lambda x: json.loads(x[1]))\
.map(lambda x: json.loads(x))\
.map(lambda x: apps(x[5], x[1], x[2], x[4], x[8] ))\
.foreachRDD(lambda x: dataresults(x))

# data.pprint()



ssc.start()
ssc.awaitTermination()