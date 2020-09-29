def udf_get_porcentaje(p_cifra_01, p_cifra_02, p_num_dec):
    return round((p_cifra_01/p_cifra_02)*100, p_num_dec)