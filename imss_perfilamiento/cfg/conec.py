import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
import pymongo
import pandas as pd
from pymongo import MongoClient
spark = SparkSession.builder.appName("PySpark").getOrCreate()

def get_df_source(archivo):
    path =archivo.ruta_src + archivo.nombre + archivo.ext
    df = spark.read.csv(path, header = archivo.encabezado, sep = archivo.separador)
   # p_nombre_archivo, header = v_header, sep = p_delimitador, engine = 'python', error_bad_lines = False
    return df

def set_df_out(datos,columnas):
    return spark.createDataFrame(datos,columnas)

def set_conn_mongo(collection):
    client = MongoClient()
    db = client.IMSS_DQ
    return db[collection]

def get_data_query(query):
    collection = set_conn_mongo(query.collection)
    return pd.DataFrame(list(collection.find(query.filter)))

def ins_data_query(query):
    collection = set_conn_mongo(query.collection)
    data = query.df.toPandas().to_dict(orient='records')
    collection.insert_many(data)