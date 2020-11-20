from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.window import Window


sc = SparkContext(appName="ReadOnly50Lines")

spark = SparkSession(sc)

### Good
# myData = spark.read\
#     .format("csv")\
#     .option("header", "true")\
#     .load("file:///home/consultant/Downloads/hr.csv")\
#     .limit(5)

### Good
# myData = spark.read\
#     .option("header", "true")\
#     .csv("file:///home/consultant/Downloads/hr.csv")\
#     .limit(6)

userSchema = StructType()\
    .add("EmpID", "string")\
    .add("DeptID", "integer")\
    .add("Salaire", "integer")\
    .add("manager", "string")\
    .add("departement", "string")

myData = spark.readStream\
        .option("sep",";")\
        .option("header", "false")\
        .schema(userSchema)\
        .csv("file:///home/consultant/Downloads/hr*.csv")

myData.createOrReplaceTempView("salaire")

totalSalary = spark.sql("select EmpID,sum(salaire) from salaire group by EmpID")

# totalSalary = myData.groupBy("EmpID").sum("salaire")

# query = totalSalary.writeStream\
#         .outputMode("complete")\
#         .format("console")\
#         .start()

# query.awaitTermination()

query = totalSalary.writeStream\
        .outputMode("append")\
        .format("parquet")\
        .queryName("salaires")\
        .option("checkpointLocation", "file:///home/consultant/Desktop/test")\
        .start("file:///home/consultant/Desktop/test")


query.awaitTermination()


# pprint(myData)
# myData.show()