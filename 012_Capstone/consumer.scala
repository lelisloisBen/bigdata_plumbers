import org.apache.spark.streaming.StreamingContext._
import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.sql._
import org.apache.spark.sql.types._
import org.apache.spark.streaming.kafka._
import java.util.Properties
import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkConf
import scala.collection.mutable.ListBuffer

class consumer
{	
	def main(args: Array[String]): Unit =
	{
		val linelist: ListBuffer[String] = new ListBuffer[String]();
	
        val ss = SparkSession.builder.appName("capstonePlayStore")\
                .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/test.playstore") \
                .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/test.playstore") \
                .getOrCreate()


		import ss.implicits._
		val sc = ss.sparkContext
 		val ssc = new StreamingContext(sc, Seconds(10))

		val sqlContext = new org.apache.spark.sql.SQLContext(sc)

		val dstream = KafkaUtils.createStream(ssc, "localhost:9092", "playstore" , Map("data"-> 1))

		
		val mappedlines = dstream.foreachRDD{ rdd =>
      		rdd.foreach{record =>
			     var mylist = List(record._2)
			     print(mylist)
			     var myrdd = sc.parallelize(mylist)		     
			     var myrdd2 = myrdd.map{x => Row( x['developerId'], x['title'], x['url'], x['priceText'], x['score'], x['scoreText'] )}
			     var df = sqlContext.createDataFrame( myrdd2 )
			     
			     if (df != null) {
                        df.write.format("mongo").mode("append").save() 
                    }
			   }
		}
		ssc.start
   		ssc.awaitTermination
	}
}