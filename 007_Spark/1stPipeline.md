# How to create pipeline from API -> KAFKA -> SPARK -> HIVE

![pipeline_construction](https://user-images.githubusercontent.com/54423322/88702092-e616f900-d0d8-11ea-9b1a-313cd7700181.jpg)

## - start zookeeper
```
zookeeper-server-start.sh -daemon /home/consultant/Desktop/opt/kafka_2.12-2.0.0/config/zookeeper.properties
```
## - start kafka in daemon mode
```
kafka-server-start.sh -daemon /home/consultant/Desktop/opt/kafka_2.12-2.0.0/config/server_twitter_spark.properties
```
## - create a Topic
```
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic kafkaNBA2
```
## - see the list of Topics
```
kafka-topics.sh --list --zookeeper localhost:2181
```
## - start Hive Metastore:

```
hive --service metastore
```
## - start Hive, show tables to see the tables and make sure it's working
```
hive
```

## - Create two files...
## - create a producer.py file that connect your API and send the message to Kafka in json format
## producer.py
```
from kafka import SimpleProducer, KafkaClient
from time import sleep
import json
from kafka import KafkaProducer
import requests
from json import dumps
import json 

kafka = KafkaClient("localhost:9096")
producer = SimpleProducer(kafka)

myheaders = {
   	"x-rapidapi-host": "free-nba.p.rapidapi.com",
	"x-rapidapi-key": "",
	"useQueryString": 'true'
}

x= requests.get('https://free-nba.p.rapidapi.com/stats', headers=myheaders)
t = x.json()
print(t)

producer.send_messages("kafkaNBA2", json.dumps(t))
```
## - create a sparkStreaming.py file that read Kafka Topic message with Spark and send to Hive
## 1stPipeline.py
```
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import sql
from pyspark.sql import SQLContext
import json

sc = SparkContext(appName="samir")                                                                                     
ssc = StreamingContext(sc, 5)          

ks = KafkaUtils.createDirectStream(ssc, ['kafkaNBA2'], {'metadata.broker.list': 'localhost:9096'})   

result1 = ks.map(lambda x: json.loads(x[1])).flatMap(lambda x: x['data']).map(lambda x: x['player'])

result1.pprint()

def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global ss                                                                                                       
        df = ss.createDataFrame(rdd, schema=['first_name','last_name', 'height_inches', 'weight_pounds','team_id','height_feet','position','id'])                                                
        df.show()                                                                                                       
        df.write.saveAsTable(name='default.nba1', format='hive', mode='append')  
                                                                                           
ss = SparkSession.builder.appName("samir").config("spark.sql.warehouse.dir", "/user/hive/warehouse/").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()                                                                                                  
ss.sparkContext.setLogLevel('WARN') 
                                
result1.foreachRDD(handle_rdd) 

ssc.start()                                                                                                             
ssc.awaitTermination()
```

## - run the spark-submit command: 
```
spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 1stPipeline.py
```
## - run the producer to send the message to Kafka Topic:
```
python producer.py
```

## SPARK should look like that:
![1st_pipeline_spark](https://user-images.githubusercontent.com/54423322/88701577-2aee6000-d0d8-11ea-83c3-fa2fa5c2e761.png)

## Select everything from the table in Hive
```
SELECT * FROM nba1;
```
## HIVE should look like that
![1st_pipeline_hive](https://user-images.githubusercontent.com/54423322/88701666-52452d00-d0d8-11ea-9010-5456120a7cbd.png)

# DONE!

![pipelineDone](https://user-images.githubusercontent.com/54423322/88702185-fd55e680-d0d8-11ea-892c-fb3dc12e7ad0.jpg)


[Samir Benzada](https://github.com/samirbenzada)