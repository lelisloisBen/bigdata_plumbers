 
from kafka import KafkaConsumer
from json import loads
import json


# f = open('Currency Exchange.txt','w')
consumer = KafkaConsumer( 'kafkaCE', bootstrap_servers=['localhost:9098'], auto_offset_reset='earliest')


result=consumer.text
result_list= result.splitlines()

print(result_list)

# print(consumer)
# for message in consumer:
# 	message = message.value
# 	f.write(message.decode("utf-8"))

print("gooooooooood")
f.close()