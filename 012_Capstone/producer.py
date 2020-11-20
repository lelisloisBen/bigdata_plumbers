from kafka import KafkaClient
import json
from kafka import KafkaProducer
import requests
from json import dumps


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

myheaders = {
   	"x-rapidapi-host": "api-playstore.p.rapidapi.com",
	"x-rapidapi-key": PLAYSTORE_KEY1,
	"useQueryString": 'true'
}

x = requests.get('https://api-playstore.p.rapidapi.com/apiv2/com.facebook.orca/similar', headers=myheaders)
t = x.json()
new = t['data']

producer.send("playstore", json.dumps(new))

print(json.dumps(new, indent=4))

    
