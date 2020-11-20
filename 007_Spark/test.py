# from pyspark.streaming.kafka import KafkaUtils

# ssc = StreamingContext(sc, 2)
# kafkaStream = KafkaUtils.createStream(ssc, [ZK quorum], [consumer group id], [per-topic number of Kafka partitions to consume])


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


sc = SparkContext(appName="PythonStreamingKafkaWordCount")
ssc = StreamingContext(sc, 1)


kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'kafkaTwitterSpark':1})

# lines = kvs.map(lambda x: x[1])
# counts = lines.flatMap(lambda line: line.split(" ")) \
#     .map(lambda word: (word, 1)) \
#     .reduceByKey(lambda a, b: a+b)
# counts.pprint()

kvs.pprint()

ssc.start()
ssc.awaitTermination()