import pyspark.sql.functions as F
def udf_unique_values(p_df_in, p_columna):
     result = p_df_in.select(F.countDistinct(p_columna)).collect()
     return int(result[0][0])