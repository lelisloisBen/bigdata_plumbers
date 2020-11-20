from time import sleep
import json
from kafka import KafkaProducer
import requests
from json import dumps
import json 

producer = KafkaProducer(bootstrap_servers=['localhost:9098'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


headers = {
   	"x-rapidapi-host": "free-nba.p.rapidapi.com",
	"x-rapidapi-key": "14a8b42a6cmshceb9a36e240a1cep1dc18ejsnf5536497b56e",
	"useQueryString": 'true'
}

x= requests.get('https://free-nba.p.rapidapi.com/stats', headers=headers)

result=x.text


for x in range(1):
	producer.send('kafkaNBA', json.dumps(result))
	print("SUCCESS")


producer.send('kafkaNBA',json.dumps(result).encode('utf-8'))