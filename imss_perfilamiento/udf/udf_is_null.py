def udf_is_null(p_columna):
    import pandas as pd

    lista_registros = []

    for i in range(len(p_columna)):
       val_cad_is_num = p_columna.values[i]
       if pd.isna(val_cad_is_num):
          lista_registros += ['1']
       else:
          lista_registros += ['0']

    return lista_registros