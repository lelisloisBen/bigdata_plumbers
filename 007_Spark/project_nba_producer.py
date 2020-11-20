from kafka import SimpleProducer, KafkaClient

from time import sleep
import json
from kafka import KafkaProducer
import requests
from json import dumps
import json 

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

myheaders = {
   	"x-rapidapi-host": "free-nba.p.rapidapi.com",
	"x-rapidapi-key": "14a8b42a6cmshceb9a36e240a1cep1dc18ejsnf5536497b56e",
	"useQueryString": 'true'
}

x= requests.get('https://free-nba.p.rapidapi.com/stats', headers=myheaders)
t = x.json()
print(t)


producer.send_messages("kafkaNBA2", json.dumps(t))

    
