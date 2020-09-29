import os, sys
from test.obj_clases import Archivo
from menu.cfg.cfg_reglas import reglas
from menu.cfg.cfg_conexion import hdfs


def udf_ayu_agr_obj_archivos(resultado):
    lis_obj_archivo = []
    lis_temp = []
    for idx, archivo in enumerate(resultado.archivos):
        if str(archivo) == str(resultado.opc_asterico):

            # opcion asterisco todos los archivos
            lis_temp = [f for f in listdir(resultado.ruta_src) if isfile(join(resultado.ruta_src, f))]
            for idy, a in enumerate(lis_temp):
                lis_obj_archivo.append(
                    Archivo(id_archivo=idy, nombre=a, separador=resultado.separador, encabezado=resultado.encabezado))
        elif isinstance(archivo, Archivo):
            lis_obj_archivo.append(Archivo(id_archivo=idx, nombre=archivo.nombre, separador=archivo.separador,
                                           encabezado=archivo.encabezado))


        else:

            lis_obj_archivo.append(
                Archivo(id_archivo=idx, nombre=archivo, separador=resultado.separador, encabezado=resultado.encabezado))
    resultado.archivos = lis_obj_archivo
    return resultado


def udf_ayu_agr_reglas(resultado):
    resultado.reglas = reglas
    return resultado


def udf_ayu_val_ori_datos(menu, resultado):
    flag = False
    if hdfs:
        if not menu:
            if hdfs.isdir(resultado.ruta_src):
                flag = True
        elif hdfs.isdir(menu.ruta_src):
            flag = True
    else:
        print("Sin conexion a servidor hdfs: {v}".format(v=hdfs), resultado.ruta_src, menu.ruta_src)
        if not menu:
            if os.path.isdir(resultado.ruta_src):
                flag = True
        elif os.path.isdir(menu.ruta_src):
            flag = True
    return flag


def udf_ayu_val_exi_archivo(archivo):
    flag = False
    if hdfs:
        if hdfs.isfile(archivo.ruta_src + archivo.nombre):
            flag = True
    else:
        if os.path.isfile(archivo.ruta_src + archivo.nombre):
            flag = True
    return flag

