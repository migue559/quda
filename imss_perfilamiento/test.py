import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("PySpark").getOrCreate()
df = spark.createDataFrame([('TX',), ('NJ',), ('TX',), ('CA',), ('NJ',)], ('state',))
result = df.groupBy('state').count().withColumn('x5', F.col('count')*2)

print(type(result))

p_valor ='   '

print('ddd'+str(p_valor).strip()+'ddddd')


#spark.createDataFrame([(1, "a", 23.0), (3, "B", -23.0)], ("x1", "x2", "x3")).withColumn("x5", exp("x3")).show()

#df.groupBy('state').count().show()

#print(type(result))
#print(result)
#print(type(result[0]))
#print(result[0][0])
#print(result[0][1])


#for item in result:
#    print(item)
#    print(item[0])
#    print(item[1])

#result2 = spark.createDataFrame([('SpeciesId', 'int', 'int'), ('SpeciesName', 'string', 'int'), ('kljkj', 'string', 'int')], ["col_name", "data_type", "data_type5"]);
#for f in result2.collect():
#    print(f[0])


#df = spark.createDataFrame([(1, "a", 23.0), (3, "B", -23.0)], ("x1", "x2", "x3"))
#df_with_x5 = df.withColumn("x5", exp("x3"))
#df_with_x5.show()

#df_result = set_df_out(lista_registros, lista_encabezado)
#lista_encabezado.clear()
#df_result2 = df_result.groupBy('Nombre_Columna', 'Patron', ).count())

#spark.createDataFrame([(1, "a", 23.0), (3, "B", -23.0)], ("x1", "x2", "x3")).withColumn("x5", exp("x3")).show()
#df_with_x5 = df.withColumn("x5", exp("x3"))