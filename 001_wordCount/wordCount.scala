val list = List("samir is working on BigData Technologies","Hello samir","BigData plumbers")

val words = list.flatMap(line => line.split(" "))

val keyData = words.map(word => (word,1))

val groupedData = keyData.groupBy(_._1)

val result = groupedData.mapValues(list=>{
    list.map(_._2).sum
})

result.foreach(println)

// create a Vertices DataFrame
val vertices = spark.createDataFrame(List(("JFK", "New York","NY"))).toDF("id", "city", "state")

// create a Edges DataFrame
val edges = spark.createDataFrame(List(("JFK", "SEA", 45, 1058923))).toDF("src", "dst", "delay", "tripID”)