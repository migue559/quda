def udf_is_length(p_columna,v_opciones_menu_limpieza):
    import pandas as pd

    lista_registros = []
    v_length = v_opciones_menu_limpieza['longitud']

    for i in range(len(p_columna)):
       val_cad_is_length= p_columna.values[i]
       if pd.isna(val_cad_is_length):
          lista_registros += [None]
       else:
           try:
               if len(val_cad_is_length)== v_length:
                   lista_registros += ["1"]
               else:
                   lista_registros += ["0"]
           except:
               lista_registros += ["0"]

    return lista_registros