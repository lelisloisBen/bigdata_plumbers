from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

ACCESS_TOKEN = "1281250352201957378-Es4zxHxNwiTFQPFihdDZKXJ7HBW7uL"
TOKEN_SECRET = "XVcL102M4L4knXtkJOelhB9r18D2M7G0EKhgux6x4ri8I"
CONSUMER_KEY = "qGYCt6WQypxgfGZn5f2yvo9ZE"
CONSUMER_SECRET = "IsxCfnLjvST8WRhsSsFZUYyLcqYLI8IFE0r3ILnLPW1a0kw8y8"

kafka = KafkaClient("localhost:9096")
producer = SimpleProducer(kafka)

class StdOutListener(StreamListener):
    def on_data(self, data):
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