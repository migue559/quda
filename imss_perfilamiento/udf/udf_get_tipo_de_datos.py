def udf_get_tipo_de_datos(p_total_nulos, p_total_int, p_total_float, p_total_date, p_total_str, p_total_blank):
    dict_tipo_datos = {'Cadena': p_total_str, 'Entero': p_total_int, 'Flotante': p_total_float, 'Fecha': p_total_date, 'Blanco': p_total_blank, 'Vacio': p_total_nulos}
    num_max_dict = max(dict_tipo_datos.values())
    for x in dict_tipo_datos.keys():
        if dict_tipo_datos[x] == num_max_dict:
            v_tipo_de_dato = x
            break
    return v_tipo_de_dato