import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("PySpark").getOrCreate()
df = spark.createDataFrame([('TX',), ('NJ',), ('TX',), ('CA',), ('NJ',)], ('state',))
#result = df.groupBy('state').count().withColumn('x5', F.col('count')*2)

#nombre = 'UMF_test'
#ext = '.txt'
#separador = '^'
#encabezado = True
#ruta_src = 'C:/Users/othon.suarez/Documents/hdfs/'

#path =ruta_src + nombre + ext
#df = spark.read.csv(path, header = encabezado, sep = separador)

#print(type(result))
#df.write.format("txt").save("UMF.txt")

#df.createOrReplaceTempView("namesPartByColor")

#sqlDF = spark.sql("SELECT * FROM namesPartByColor")
df.show()