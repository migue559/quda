from cfg.conec import get_df_source,set_df_out,get_data_query
from udf.udf_tipo_float import udf_tipo_float
from udf.udf_tipo_int import udf_tipo_int
from udf.udf_get_tipo_de_datos import udf_get_tipo_de_datos
from udf.udf_get_porcentaje import udf_get_porcentaje
from udf.udf_tipo_date import udf_tipo_date
from udf.udf_get_estadisticas import udf_get_estadisticas
from udf.udf_null_values import udf_null_values
from udf.udf_unique_values import udf_unique_values
from udf.udf_isblank import udf_isblank
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import pandas as pd
from operator import sub
from obj.obj_clases import queryMongo

import pyspark.sql.functions as F
import re

class profiling(object):

    def statistics_data_type(archivo):

        df_data_type = spark_df_source = get_df_source(archivo)

        lista_encabezado = ['Nombre_Archivo'
                           ,'Nombre_Columna'
                           ,'Nulos'
                           ,'Porc_Nulos'
                           ,'Blancos'
                           ,'Porc_Blancos'
                           ,'Unicos'
                           ,'Porc_Unicos'
                           ,'Tipo_Dato'
                           ,'Frec_enteros'
                           ,'Porc_Enteros'
                           ,'Frec_flotantes'
                           ,'Porc_Flotantes'
                           ,'Frec_fechas'
                           ,'Porc_Fechas'
                           ,'Frec_cadenas'
                           ,'Porc_Cadenas'
                           ,'Long_Max'
                           ,'Long_Min'
                           ,'Val_Max'
                           ,'Val_Min'
                           ,'Media'
                           ,'Desv_Estandar'
                            ]
        lista_conteos = []
        v_no_aplica = 'n/a'
        p_num_rows_df = df_data_type.count()

        v_nombre_archivo = archivo.nombre
        for i in range(len(df_data_type.columns)):

            v_total_int = 0
            v_total_float = 0
            v_total_date = 0
            v_total_str = 0
            v_total_blank = 0
            v_total_vacio = 0

            lista_cadenas = []
            lista_enteros = []
            lista_float = []
            lista_fechas = []
            lista_blank  = []

            v_nombre_columna = df_data_type.columns[i]
            v_total_unicos = udf_unique_values(df_data_type, v_nombre_columna)
            tupla_total_nulos = udf_null_values(df_data_type, v_nombre_columna)
            v_total_nulos = tupla_total_nulos[0]
            serie_valores_unicos = df_data_type.groupBy(v_nombre_columna).count().collect()

            for item in serie_valores_unicos:
                 v_valor_columna = item[0]
                 v_frec_valor = item[1]

                 if udf_tipo_int(v_valor_columna) == True:
                     v_total_int += v_frec_valor
                     lista_enteros.append(int(v_valor_columna))
                 else:
                     if udf_tipo_float(v_valor_columna) == True:
                         v_total_float += v_frec_valor
                         lista_float.append(float(v_valor_columna))
                     else:
                         if udf_tipo_date(v_valor_columna) == True:
                             v_total_date += v_frec_valor
                             lista_fechas.append(v_valor_columna)
                         else:
                             if udf_isblank(v_valor_columna) == True:
                                 v_total_blank += v_frec_valor
                                 lista_blank.append(v_valor_columna)
                             else:
                                 if v_valor_columna is None:
                                     v_total_vacio += v_frec_valor
                                 else:
                                     v_total_str += v_frec_valor
                                     lista_cadenas.append(v_valor_columna)

            v_tipo_de_dato = udf_get_tipo_de_datos(v_total_vacio, v_total_int, v_total_float, v_total_date, v_total_str,v_total_blank)

            if (v_tipo_de_dato == 'Entero'):
                lista_estadisticas = udf_get_estadisticas(v_tipo_de_dato, lista_enteros, 6)
            if (v_tipo_de_dato == 'Flotante'):
                lista_estadisticas = udf_get_estadisticas(v_tipo_de_dato, lista_float, 6)
            if (v_tipo_de_dato == 'Fecha'):
                lista_estadisticas = udf_get_estadisticas(v_tipo_de_dato, lista_fechas, 6)
            if (v_tipo_de_dato == 'Cadena'):
                lista_estadisticas = udf_get_estadisticas(v_tipo_de_dato, lista_cadenas, 6)
            if (v_tipo_de_dato == 'Vacio' or v_tipo_de_dato =='Blanco'):
                lista_estadisticas = ['0', '0', v_no_aplica, v_no_aplica, v_no_aplica, v_no_aplica]

            v_porc_int = udf_get_porcentaje(v_total_int, p_num_rows_df, 6)
            v_porc_float = udf_get_porcentaje(v_total_float, p_num_rows_df, 6)
            v_porc_date = udf_get_porcentaje(v_total_date, p_num_rows_df, 6)
            v_porc_str = udf_get_porcentaje(v_total_str, p_num_rows_df, 6)
            v_porc_unicos = udf_get_porcentaje(v_total_unicos, p_num_rows_df, 6)
            v_porc_nulos = udf_get_porcentaje(v_total_nulos, p_num_rows_df, 6)
            v_porc_blank = udf_get_porcentaje(v_total_blank, p_num_rows_df, 6)

            lista_conteos += [
                [v_nombre_archivo,v_nombre_columna, v_total_nulos, v_porc_nulos, v_total_blank, v_porc_blank, v_total_unicos,
                 v_porc_unicos, v_tipo_de_dato, v_total_int, v_porc_int, v_total_float, v_porc_float,
                 v_total_date, v_porc_date, v_total_str, v_porc_str] + lista_estadisticas]

        return set_df_out(lista_conteos, lista_encabezado)

    def statistics_data_frequency(archivo):

        df_frequency = spark_df_source = get_df_source(archivo)

        lista_encabezado = ['Nombre_Archivo','Nombre_Columna', 'Valores', 'Frec_valores', 'Porc_Valor']
        lista_registros = []
        count_rows = df_frequency.count()

        v_nombre_archivo = archivo.nombre
        for i in range(len(df_frequency.columns)):

            v_nombre_columna = df_frequency.columns[i]
            tupla_total_nulos = udf_null_values(df_frequency, v_nombre_columna)
            v_frec_valor = tupla_total_nulos[0]

            if v_frec_valor > 0:
                v_valor_unico = 'Vacio'
                v_porc_valor = udf_get_porcentaje(v_frec_valor, count_rows, 6)
                lista_registros += [[v_nombre_columna, v_valor_unico, v_frec_valor, v_porc_valor]]

            if tupla_total_nulos[1] > 0:
                result =  df_frequency.groupBy(v_nombre_columna).count().collect()
                for item in result:
                    v_valor_unico = item[0]
                    v_frec_valor =  item[1]
                    v_porc_valor = udf_get_porcentaje(v_frec_valor, count_rows, 6)
                    lista_registros += [[v_nombre_archivo,v_nombre_columna, v_valor_unico, v_frec_valor, v_porc_valor]]

        return set_df_out(lista_registros, lista_encabezado)

    def statistics_data_pattern(archivo):

        df_pattern = df_frequency = spark_df_source = get_df_source(archivo)

        lista_encabezado = ['Nombre_Archivo','Nombre_Columna', 'Patron']
        lista_registros = []
        pattern = '[\d]+|[a-zA-ZñÑ]+|[><#,$.¡!°~{_?-]+|[^\da-zA-ZñÑ><#,$.¡!°~{_?-]+'
        num_rows = df_pattern.count()

        v_nombre_archivo = archivo.nombre
        for i in range(len(df_pattern.columns)):

            v_nombre_columna = df_pattern.columns[i]
            for f in df_pattern.collect():
                v_valor_columna = f[i]
                patron = ''
                for substr in re.findall(pattern, v_valor_columna):
                    if (re.search('[a-zA-ZñÑ]+', substr)):
                        prefix = 'A'
                    elif (re.search('[\d]+', substr)):
                        prefix = '1'
                    elif (re.search('[><#,$.¡!°~{_?-]+', substr)):
                        prefix = 'S'
                    if (re.search('[^\da-zA-ZñÑ><#,$.¡!°~{_?-]+', substr)):
                        prefix = substr
                        leng = ''
                    else:
                        leng = '(' + str(len(substr)) + ')'
                    patron = patron + prefix.replace(" ", "B") + leng
                if (len(patron) == 0): patron = 'vacio'
                lista_registros += [[v_nombre_archivo,v_nombre_columna,patron]]

        df_result = set_df_out(lista_registros, lista_encabezado)
        df_pattern_out = df_result.groupBy('Nombre_Archivo','Nombre_Columna', 'Patron',).count().withColumn('Porc_Patron',(F.col('count')/num_rows)*100).collect()
        return set_df_out(df_pattern_out,['Nombre_Archivo','Nombre_Columna', 'Patron','Frec_Valores'])

    def graph_data_frequency(reporte):
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{v:d}\n{p:.2f}%'.format(p=pct, v=val)
            return my_autopct

        filt_dict = {"Id_Configuracion": reporte.id_configuracion}
        querymongo = queryMongo('statistics_profiling', filt_dict,)
        data_sp = get_data_query(querymongo)

        data_sp['Fecha_Registro'] = pd.to_datetime(data_sp['Fecha_Registro'], format='%d/%m/%Y')
        data_sp.sort_values(by=['Fecha_Registro'], inplace=True, ascending=True)
        data_sp.groupby(['Columna', 'Funcion', 'Fecha_Registro'])[["Registros_Analizados", "Registros_Funcion", "Porc_Funcion"]].apply(sum)
        data_sp['Fecha_Registro'] = data_sp['Fecha_Registro'] .dt.strftime('%d/%m/%Y')

        periodo = data_sp['Fecha_Registro'].to_list()
        registros = data_sp['Registros_Analizados'].to_list()
        total_registros = [int(i) for i in registros]
        registros_funcion = data_sp['Registros_Funcion'].to_list()
        total_registros_funcion = [int(i) for i in registros_funcion]
        dif_registros_funcion = list(map(sub, total_registros, total_registros_funcion))

        total_reg = len(data_sp)
        if (total_reg > 10):
            del periodo[1:total_reg-9]
            del total_registros_funcion[1:total_reg-9]
            del dif_registros_funcion[1:total_reg-9]

        funcion_cantidad_periodo= {
            'SI': total_registros_funcion,
            'NO': dif_registros_funcion,
        }

        fig, ax = plt.subplots(1, 2)
        ax[0].stackplot(periodo, funcion_cantidad_periodo.values(), labels=funcion_cantidad_periodo.keys())
        ax[0].legend(title=reporte.funcion,loc='upper center')
        ax[0].set_title('Historico de la Funcion')
        ax[0].set_xlabel('Fecha de Ejecucion del Analisis')
        ax[0].set_ylabel('Numero de Registros')
        ax[0].tick_params(axis='x', labelsize=8)
        ax[0].tick_params(axis='y', labelsize=8)
        ax[0].figure.autofmt_xdate()

        porc_total_registros_funcion = total_registros_funcion[len(total_registros_funcion) - 1]
        porc_dif_registros_funcion = dif_registros_funcion[len(dif_registros_funcion) - 1]
        last_periodo = periodo[len(periodo) - 1]
        date_porc = [porc_total_registros_funcion, porc_dif_registros_funcion]
        validacion = ['SI', 'NO']
        explode = (0, 0.1)

        wedges, texts, autotexts = ax[1].pie(date_porc,radius=.7, explode=explode,autopct=make_autopct(date_porc), textprops={'color': 'w'}, shadow=True)
        ax[1].legend(wedges, validacion, title=reporte.funcion, loc="upper center")
        ax[1].set_title("Source: "+reporte.archivo+"/"+reporte.columna+"/"+reporte.parametro+" al "+last_periodo)

        plt.gcf().canvas.set_window_title('Estadistica Calidad de Datos '+reporte.funcion)
        plt.setp(autotexts, size=8, weight="bold")
        plt.show()