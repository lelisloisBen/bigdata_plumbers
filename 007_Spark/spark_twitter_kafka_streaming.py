"""

Run kafka_twitter_spark_streaming.py (Start Consumer)
spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10:2.12-2.4.4 ~/home/consultant/Desktop/bigdata_plumbers/007_Spark/spark_twitter_kafka_streaming.py


spark-streaming-kafka-0-10


JAR file to download and paste in /Desktop/opt/spark-2.4.4/jars
https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10_2.12/2.4.4


"""

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

if __name__ == "__main__":

	#Create Spark Context to Connect Spark Cluster
    sc = SparkContext(appName="PythonStreamingKafkaTweetCount")

	#Set the Batch Interval is 10 sec of Streaming Context
    ssc = StreamingContext(sc, 10)

	#Create Kafka Stream to Consume Data Comes From Twitter Topic
	#localhost:2181 = Default Zookeeper Consumer Address
    kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming', {'kafkaTwitterSpark':1})
    
    #Parse Twitter Data as json
    parsed = kafkaStream.map(lambda v: json.loads(v[1]))

	#Count the number of tweets per User
    user_counts = parsed.map(lambda tweet: (tweet['user']["screen_name"], 1)).reduceByKey(lambda x,y: x + y)

	#Print the User tweet counts
    user_counts.pprint()

	#Start Execution of Streams
    ssc.start()
    ssc.awaitTermination()

