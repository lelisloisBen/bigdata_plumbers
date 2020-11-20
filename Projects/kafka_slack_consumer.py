 
from kafka import KafkaConsumer
from json import loads
import json


f = open('simpsons.txt','w')
consumer = KafkaConsumer( 'kafkaSlack', bootstrap_servers=['localhost:9098'], auto_offset_reset='earliest')

print(consumer)
for message in consumer:
	message = message.value
	f.write(message.decode("utf-8"))

print("gooooooooood")
f.close()