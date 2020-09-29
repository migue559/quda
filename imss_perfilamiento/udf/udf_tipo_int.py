def udf_tipo_int(p_valor):
    try:
        int(str(p_valor))
        return True
    except:
        return False