from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from collections import namedtuple
from pyspark.sql import SparkSession
import re 
import random

from unidecode import unidecode

spark = SparkSession.builder.appName("WordCountSpark").getOrCreate()

sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 10)

lines = ssc.textFileStream("hdfs://localhost:9000//pipeline1")


def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))
 
lines.foreachRDD(remove_non_ascii) 


lines.pprint()

ssc.start()
ssc.awaitTermination()