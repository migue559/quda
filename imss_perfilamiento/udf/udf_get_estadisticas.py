def udf_get_estadisticas(p_tipo_de_dato, p_lista_valores, p_num_dec):
    import statistics as sd
    v_no_aplica = 'n/a'
    v_val_media = v_no_aplica
    v_val_stdev = v_no_aplica
    lista_longitudes = []
    try:
        v_val_max = max(filter(None.__ne__, p_lista_valores))
    except:
        v_val_max=''
    try:
        v_val_min = min(filter(None.__ne__, p_lista_valores))
    except:
        v_val_min=''

    v_num_elementos = len(p_lista_valores)
    for i in range(v_num_elementos):
       v_longitud_valor = len(str(p_lista_valores[i]))
       lista_longitudes.append(v_longitud_valor)
    v_long_max = max(lista_longitudes)
    v_long_min = min(lista_longitudes)
    if (p_tipo_de_dato == 'Entero') or (p_tipo_de_dato == 'Flotante'):
        v_val_media = round(sd.mean(p_lista_valores),p_num_dec)
        if len(p_lista_valores) > 1:
            v_val_stdev = round(sd.stdev(p_lista_valores),p_num_dec)
    return [str(v_long_max), str(v_long_min), str(v_val_max),str(v_val_min), str(v_val_media), str(v_val_stdev)]