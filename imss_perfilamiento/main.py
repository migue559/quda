from profiling import profiling
from obj.obj_clases import File,Reporte,queryMongo
from pymongo import MongoClient
from cfg.conec import ins_data_query

nombre = 'UMF_test_2'
ext = '.txt'
separador = '^'
encabezado = True
ruta_src = 'C:/Users/othon.suarez/Documents/hdfs/'

archivo = File(nombre, ext, separador, encabezado, ruta_src)

out_profiling_data_type = profiling.statistics_data_type(archivo)
querymongo = queryMongo('profiling_data_type','',out_profiling_data_type)
ins_data_query(querymongo)

out_profiling_frequency = profiling.statistics_data_frequency(archivo)
querymongo = queryMongo('profiling_frequency','',out_profiling_frequency)
ins_data_query(querymongo)

out_profiling_pattern = profiling.statistics_data_pattern(archivo)
querymongo = queryMongo('profiling_pattern','',out_profiling_pattern)
ins_data_query(querymongo)

reporte = Reporte('2','UMF','CP','IS_NUMBER','')
#reporte = Reporte('3','DIAGNOSTICO','ENFERMEDAD','IS_NUMBER','P')
profiling.graph_data_frequency(reporte)