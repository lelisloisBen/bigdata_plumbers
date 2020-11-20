from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


sc = SparkContext(appName="WordCountSpark")
ssc = StreamingContext(sc, 1)

lines = ssc.textFileStream("hdfs://localhost:9000//pipeline1/")
words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
#wordCounts.print()
words.saveAsTextFiles("/home/consultant/Desktop/")
ssc.start()
ssc.awaitTermination()