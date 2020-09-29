def udf_tipo_date(p_valor):
    from datetime import datetime
    tupla_formato_fecha = ('%d/%m/%Y %H:%M:%S','%d/%m/%y %H:%M:%S',
                           '%m/%d/%Y %H:%M:%S','%m/%d/%y %H:%M:%S',
                           '%d-%m-%Y %H:%M:%S','%d-%m-%y %H:%M:%S',
                           '%m-%d-%Y %H:%M:%S','%m-%d-%y %H:%M:%S',
                           '%Y/%m/%d %H:%M:%S','%y/%m/%d %H:%M:%S',
                           '%Y-%m-%d %H:%M:%S','%y-%m-%d %H:%M:%S',
                           '%d/%m/%Y','%d/%m/%y',
                           '%m/%d/%Y','%m/%d/%y',
                           '%d-%m-%Y','%d-%m-%y',
                           '%m-%d-%Y','%m-%d-%y',
                           '%Y/%m/%d','%y/%m/%d',
                           '%Y-%m-%d','%y-%m-%d')
    v_num_elementos_tupla = len(tupla_formato_fecha)
    v_valor_verdad = False
    for i in range(v_num_elementos_tupla):
            try:
                datetime.strptime(p_valor,tupla_formato_fecha[i])
                v_valor_verdad = True
                break
            except:
                continue
    else:
        v_valor_verdad = False
    return v_valor_verdad