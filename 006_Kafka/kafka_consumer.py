from kafka import KafkaConsumer
from json import loads

f = open('new_one.txt','w')
consumer = KafkaConsumer( 'bigdata', bootstrap_servers=['localhost:9098'], auto_offset_reset='earliest')

for message in consumer:
	message = message.value
	f.write(message.decode("utf-8"))


print("gooooooooood")
f.close()