from pyspark import SparkContext
sc = SparkContext(appName="WordCountSparkAirflow")
text_file = sc.textFile("hdfs://localhost:9000/twitter_data/FlumeData.1595603063817")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("/home/consultant/Desktop/bigdata_plumbers/013_Airflow/wordcount_result")