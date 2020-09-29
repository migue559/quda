import findspark
findspark.init()
import pyspark
from os.path import join, abspath
from pyspark.sql import SparkSession
from pyspark.sql import Row

# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration") \
    #.config("hive.metastore.uris", "thrift://localhost:9083")
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()
print(spark)
print(spark.sql("SELECT 1 "))
#print(spark.sql("create table test_rev (aa,bb) "))

#spark.sql("CREATE TABLE IF NOT EXISTS mydatabase.students(name string,age int)")

#data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
#df = spark.createDataFrame(data)
# Write into Hive
#df.write.saveAsTable('example')

#df_load = sparkSession.sql('SELECT * FROM example')
#df_load.show()
#print(df_load.show())











