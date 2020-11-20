from time import sleep
from json import dumps
import json
from kafka import KafkaProducer
import requests



producer = KafkaProducer(bootstrap_servers=['localhost:9098'])

headers = {
   
}
x= requests.get('https://myallies-breaking-news-v1.p.rapidapi.com/news/cnn', headers=headers)
result=x.text
result_list= result.splitlines()

print(result)
for x in range(5):
	producer.send('kafkaSlack', result.encode('utf-8'))
	print("SUCCESS")