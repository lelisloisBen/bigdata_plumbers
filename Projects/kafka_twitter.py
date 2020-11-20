from time import sleep
from json import dumps
import json
from kafka import KafkaProducer
import requests



producer = KafkaProducer(bootstrap_servers=['localhost:9098'])

headers = {
    'Authorization': 'AAAAAAAAAAAAAAAAAAAAAFxvFwEAAAAAb5Ioj5Dny8I01AzcaaZ5tKP0u4k%3Drsk2xIAt45PDEwqYuhXQARovFUvagMez2XMlsOxTeWIcH6YtLJ'
}
x= requests.get('https://api.twitter.com/labs/2/tweets/search?query=snow', headers=headers)
result=x.text
result_list= result.splitlines()

print(result)
for x in range(5):
	producer.send('kafkaSlack', result.encode('utf-8'))
	print("SUCCESS")