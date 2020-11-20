from pyspark.streaming import StreamingContext
from pyspark import SparkContext, SparkConf
from pyspark.streaming.flume import FlumeUtils


sc =SparkContext()
ssc = StreamingContext(sc,5)
flumeStream = FlumeUtils.createStream(ssc, "localhost", 6669)


flumeStream.pprint()
 
ssc.start()
ssc.awaitTermination()