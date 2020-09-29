import sys
import os, json
from datetime import datetime


import pyspark
from   pyspark.sql.types      import *
from   pyspark.sql.functions  import lower, col , current_date,unix_timestamp,to_date,lit
from   pyspark.sql            import SQLContext
from   hdfs3                  import HDFileSystem
from   cfg.cfg_par_pyspark    import cfg_obt_par_pyspark

import pandas as pd
from dateutil.parser import parse
#from pyspark.sql import SparkSession



def ejempo_lee_local_genera_df():
  file_txt=sc.textFile(src_1)
  header = file_txt.first()
  #file_txt = file_txt.filter(lambda line: line != header)
  #print("header","\n",header.split("^"))
  header_list=[]
  for idx,elem in enumerate(header.split("^")):
    header_list.append("field"+str(idx+1))
  temp_var = file_txt.map(lambda k: k.split("^"))
  #here's where the changes take place
  #this creates a dataframe using whatever pyspark feels like using (I think string is the default). 
  #the header.split is providing the names of the columns
  df=temp_var.toDF(header_list)
  print(type(df))

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

def cadena_to_date(value):
  date = None
  if value.isdigit():
    date=value
  else:
    try:
      if not is_date(value):
        date =value
      else:
        date = parse(value, fuzzy=True).strftime('%d/%m/%Y-%H:%M:%S.%f')
    except:
      date = value
  return date

def fecha_proceso():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ('.0')




args =sys.argv[1:]
par = cfg_obt_par_pyspark(args[0])

print(type(par))
print((par))

conf={'hadoop.security.authentication': 'kerberos','hadoop.rpc.protection':'authenticate'}
ticket_path_keytab='/home/centos/Documents/KeyTab/usrjaga1.keytab'
ticket_path_cache='FILE:/tmp/krb5cc_1000'  
hdfs=HDFileSystem(host='10.100.6.82'
                 ,port=8020
                 ,principal='jaga1@IMMS.GOB.MX'
                 ,driver='libhdfs'
                 ,pars=conf
                 ,ticket_cache=ticket_path_cache
                 )

path_src=par['archivo']['ruta_src']
fileName=par['archivo']['nombre']
src = path_src+fileName



conf = pyspark.SparkConf().setAppName("trn_arc_pyspark").setMaster("local[2]")
sc   = pyspark.SparkContext(conf=conf)
sqlCtx = SQLContext(sc)
sqlCtx.udf.register('udf_cadena_to_date', cadena_to_date)
sqlCtx.udf.register('udf_fecha_proceso', fecha_proceso)
fecha_proceso

#log
sc.setLogLevel('WARN')
sc.setLogLevel('ERROR')

print("HOLA", datetime.now())

"""
mySchema= StructType([
 StructField("id"                                    ,StringType(),True) ,StructField("timestamp_DB"                         ,StringType(),True) \
,StructField("SRA_id_sinolave"                      ,StringType(),True) ,StructField("fecha_captura"                        ,StringType(),   True) ])
"""
print("INI LECTURA SERVIDOR", datetime.now())
with hdfs.open(src, 'rb') as f: 
  pd_df = pd.read_csv(f, sep='^', header=None)
print("FIN LECTURA SERVIDOR", datetime.now())



string_antes = [ x for x in range(len(pd_df. columns))]
string_despues = [ 'column_'+str(x) for x in range(len(pd_df. columns))]
pd_df[ string_antes ] = pd_df[string_antes].astype(str)

pd_df.columns = string_despues

#sp_df = sqlCtx.createDataFrame(pd_df, schema=mySchema)
sp_df = sqlCtx.createDataFrame(pd_df)



"""
print(type(sp_df))
sp_df.show()
sp_df.printSchema()
print(sp_df.dtypes)
"""
print("INI PROCESO", datetime.now())

sp_df.createOrReplaceTempView('LOWER')

str_query_lower = 'SELECT '
for columna in string_despues:
    str_query_lower+=  'lower('+columna+') as '+columna+', '
str_query_lower=str_query_lower[:-2]+ ' from LOWER'


sp_df= sqlCtx.sql(str_query_lower)
sp_df.createOrReplaceTempView('TRIM')

str_query_trim = 'SELECT '
for columna in string_despues:
    str_query_trim+=  'trim('+columna+') as '+columna+', '
str_query_trim=str_query_trim[:-2]+ ' from TRIM'


sp_df= sqlCtx.sql(str_query_trim)
sp_df.createOrReplaceTempView('DATE')

"""
str_query_date = 'SELECT '
for idx, col in enumerate(string_despues):
  # evita la columna de fh_carga 
  if idx +1 != len(string_despues):   
    str_query_date+=  'udf_cadena_to_date('+col+') as '+col+', '
  else:
    str_query_date+=  ''+col+' as '+col+', '
str_query_date=str_query_date[:-2]+ ', udf_fecha_proceso() as fh_proceso from DATE'

print(str_query_date)
"""



#sp_df=sqlCtx.sql(str_query_date)
sp_df.createOrReplaceTempView('SALIDA')

#sp_df=sqlCtx.sql('SELECT column_26,fh_proceso from SALIDA')

sp_df.cache().count()
print("FIN PROCESO", datetime.now())
sp_df.show()

print("INI EXPORT CSV", datetime.now())
sp_df.repartition(1).write.format('com.databricks.spark.csv').save("part-m-00000",header = 'false')
print("FIN EXPORT CSV", datetime.now())




print("Listo",datetime.now())

