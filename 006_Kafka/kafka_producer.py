from time import sleep
from json import dumps
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9098'])
f = open('Shakespeare.txt', 'r')
line_list = f.readlines()

for e in range(len(line_list)):
	producer.send('bigdata',json.dumps(line_list[e]).encode('utf-8'))
	sleep(1)

print("good")