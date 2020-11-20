from kafka import KafkaProducer
import json
from json import dumps


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
# producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open('playstore.json') as f:
  data = json.load(f)

# print(data)

new = data['data']

# mydata = map(lambda d: (d['title'],d['url'],d['priceText'], d['score'], ), new)

# print(json.dumps(mydata, indent=4))
producer.send("CapstoneSamirTest", json.dumps(new))

print(json.dumps(new, indent=4))




