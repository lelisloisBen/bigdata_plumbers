# Ingesting Data from Twitter with Kafka to Spark (Python)

### make sure to download the right version of JAR file
(https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-8-assembly_2.11/2.4.4)
### Some Spark Documentation
(http://spark.apache.org/docs/2.1.0/streaming-kafka-0-8-integration.html)
(http://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.kafka.KafkaUtils)

### Start Zookeeper
### Start Kafka
### Create New Topic

### Create two python files
### - Producer ( for Kafka to ingest from Twitter )
### - Consumer ( for Spark to read the topic of Kafka)

## Producer.py
### you may need to install tweepy, you need to install pip first then tweepy

```
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

ACCESS_TOKEN = "your Twitter access token"
TOKEN_SECRET = "your Twitter token secret"
CONSUMER_KEY = "your Twitter consumer key"
CONSUMER_SECRET = "your Twitter consumer secret"

# replace your ip address and port use by the broker from kafka conf
kafka = KafkaClient("localhost:9096")

producer = SimpleProducer(kafka)

class StdOutListener(StreamListener):
    def on_data(self, data):
        # replace "kafkaTwitterSpark" by your Topic Name
        producer.send_messages("kafkaTwitterSpark", data.encode('utf-8'))
        # print(data)
        return True
    def on_error(self, status):
        print(status)
    
print("ingesting data...")

l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track="miami")
```

## Consumer.py

```
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# choose a name for the app
sc = SparkContext(appName="PythonStreamingKafkaWordCount")

# streaming window of 1 second
ssc = StreamingContext(sc, 1)

# creating the strean:
# Documentation: http://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.kafka.KafkaUtils
#   - StreamingContext
#   - Zookeeper quorum (hostname:port)
#   - The group id for this consumer
#   - {topic_name -> numPartitions} 

kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'kafkaTwitterSpark':1})

# print your stream
kvs.pprint()

ssc.start()
ssc.awaitTermination()
```

## Start Ingesting From Twitter to Kafka first
```
python producer.py
```

## Start Streaming From Spark
## Include the JAR File to the spark-submit
```
spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar consumer.py
```
## for hadoop 2.8.0
```
spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 consumer.py
```
![twitter_kafka](https://user-images.githubusercontent.com/54423322/88220618-33a2ea00-cc31-11ea-9df3-6ce831528620.png)

[Samir Benzada](https://github.com/samirbenzada)

