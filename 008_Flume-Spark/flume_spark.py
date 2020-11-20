# from pyspark.streaming import StreamingContext
# from pyspark import SparkContext
# from pyspark.streaming.flume import FlumeUtils


# sc = SparkContext()
# ssc = StreamingContext(sc, 10)
# flumeStream = FlumeUtils.createStream(ssc, "localhost", 6669)

# result = flumeStream.map(lambda x: json.loads(x[1]))

# result.pprint()
 
# ssc.start()
# ssc.awaitTermination()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

sc = SparkContext(appName="PythonStreamingFlumeWordCount")
ssc = StreamingContext(sc, 10)


kvs = FlumeUtils.createStream(ssc, "localhost", int(6669))
lines = kvs.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a+b)
counts.pprint()

ssc.start()
ssc.awaitTermination()