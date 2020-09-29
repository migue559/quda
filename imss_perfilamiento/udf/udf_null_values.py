from pyspark.sql.functions import isnan, when, count, col
def udf_null_values (p_df_in, p_columna):
   count_null = p_df_in.filter(p_df_in[p_columna].isNull() | isnan(p_df_in[p_columna])).count()
   count_not_null = p_df_in.filter(p_df_in[p_columna].isNotNull()).count()
   tupla_conteos = (count_null,count_not_null)

   return tupla_conteos