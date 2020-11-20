from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from collections import namedtuple
import re 
import random
## Reload the system to make sure of the encoding in utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

spark = SparkSession.builder.appName("WordCountSpark").getOrCreate()
sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 20)
firstRDD = ssc.textFileStream("hdfs://localhost:9000//pipeline1")

def toSQL(df):
	df.show()
	df.write.format("jdbc")\
	.mode("overwrite")\
	.option("url", "jdbc:mysql://localhost:3306/hadoop_test") \
	.option("dbtable", "ht") \
	.option("user", "sqoop_user") \
	.option("password", "Welcome2BB") \
	.option("driver", "com.mysql.jdbc.Driver") \
	.save()

def savetheresult( rdd ):
    if not rdd.isEmpty():
    	df = spark.createDataFrame(rdd)
    	toSQL(df)
 
fields = ("id","hashtag", "count", "length" )
Tweet = namedtuple( 'Tweet', fields )

counts = firstRDD.flatMap( lambda text: text.split( ' ' ))\
.filter( lambda word: word.lower().startswith('#') )\
.map(lambda word: word.replace('#',''))\
.filter(lambda word: re.sub('[^a-z]', ' ', word))\
.filter(lambda word: len(word)>1)\
.map( lambda word: ( word, 1 ) )\
.reduceByKey( lambda a, b: a + b )\
.map( lambda x: Tweet( random.randint(1,100000) ,x[0], x[1], len(x[0]) ) )\
.foreachRDD(lambda x: savetheresult(x))

ssc.start()
ssc.awaitTermination()