## sudo apt install python-pip
## pip install pykafka
## pip install tweepy


import pykafka
from pykafka import KafkaClient
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#TWITTER API CONFIGURATIONS
# consumer_key = twitter_config.consumer_key
# consumer_secret = twitter_config.consumer_secret
# access_token = twitter_config.access_token
# access_secret = twitter_config.access_secret

consumer_key = "qGYCt6WQypxgfGZn5f2yvo9ZE"
consumer_secret = "IsxCfnLjvST8WRhsSsFZUYyLcqYLI8IFE0r3ILnLPW1a0kw8y8"
access_token = "1281250352201957378-Es4zxHxNwiTFQPFihdDZKXJ7HBW7uL"
access_secret = "XVcL102M4L4knXtkJOelhB9r18D2M7G0EKhgux6x4ri8I"

#TWITTER API AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Twitter Stream Listener
class KafkaPushListener(StreamListener):          
	def __init__(self):
		#localhost:9092 = Default Zookeeper Producer Host and Port Adresses
		self.client = pykafka.KafkaClient("localhost:9096")
		
		#Get Producer that has topic name is kafkaTwitterSpark
		self.producer = self.client.topics[bytes("kafkaTwitterSpark")].get_producer()
  
	def on_data(self, data):
		#Producer produces data for consumer
		#Data comes from Twitter
		self.producer.produce(bytes(data))
		return True
                                                                                                                                           
	def on_error(self, status):
		print(status)
		return True

#Twitter Stream Config
twitter_stream = Stream(auth, KafkaPushListener())

#Produce Data that has miami hashtag (Tweets)
twitter_stream.filter(track=['#miami'])