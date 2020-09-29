def udf_tipo_float(p_valor):
    try:
        float(p_valor)
        return True
    except:
        return False

