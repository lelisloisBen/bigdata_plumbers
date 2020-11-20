from kafka import KafkaProducer
import json
from json import dumps


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

with open('/home/consultant/Desktop/bigdata_plumbers/013_Airflow/playstore_airflow.json') as f:
  data = json.load(f)

new = data['data']

producer.send("AirflowPlaystore", json.dumps(new))




