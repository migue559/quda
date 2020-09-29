import sys
import os

from hdfs3 import HDFileSystem
import pandas as pd


conf={'hadoop.security.authentication': 'kerberos','hadoop.rpc.protection':'authenticate'}
ticket_path_keytab='/home/centos/Documents/KeyTab/usrjaga1.keytab'
ticket_path_cache='FILE:/tmp/krb5cc_1000'  
hdfs=HDFileSystem(host='10.100.6.82'
	              ,port=8020
	              ,principal='jaga1@IMMS.GOB.MX'
	              ,driver='libhdfs'
	              ,pars=conf
	              ,ticket_cache=ticket_path_cache
	              )


#path_src='/dev/la/la_aficobranza/H_SINDO_SSCI_CUENTA_INDIVIDUAL/'
#path_src='/dev/la/la_siais/TBATENCION/'
path_src='/dev/la/la_siais/TBALTERACION/'
fileName='part-m-00000'


src =path_src+fileName



print(hdfs.ls(path_src))
print(hdfs.isfile(src))

#hdfs.get(src,fileName+'_H_SINDO_SSCI_CUENTA_INDIVIDUAL' )
#hdfs.get(src,fileName+'_TBATENCION' )
hdfs.get(src,fileName+'_TBALTERACION' )





#print(hdfs.info(CAT_UMF_src))





"""
#print(hdfs.rm(delete_file))
	  df = pd.read_csv(f, sep='^', header=None)
with hdfs.open(src, 'rb') as f:		  
df.columns = ['id','timestamp_DB','SRA_id_sinolave','fecha_captura','fecha_ingreso','organizacion','cve_delegacion','nom_delegacion','cve_deloin','cve_unidad','clues','nom_unidad','pac_appaterno','pac_apmaterno','pac_nombre','pac_CURP','CURP','pac_edad','pac_meses','pac_genero','nacionalidad','pac_domicilio','pac_telefono','pac_familiar','Origen_ingreso','diagnostico','estado_gravedad','cama','plan','fechaEgreso','nombreCargoQuienRealizoEgreso','unidadesImss','Origen_ingreso_esp','pac_derechoabiente','pac_nss','fenomeno_origen','fecha_egreso','estatus','plan_traslado','Destino_traslado','plan_hospitalizacion','observaciones','pac_conocido','desc_edad','desc_estatura','desc_complexion','desc_cara','desc_piel','desc_cabello1','desc_cabello2','desc_ojos','desc_ojos_otro','desc_senas','triage','corporal','corporal_otro','medico','tags','latitud','longitud','rastreado','FUENTE','ip_entrada','ip_salida','id_contingencia','SRA_id_Secretaria_Salud','SRA_paciente_situacion_actual','SRA_paciente_con_ventilacion_mecanica','SRA_paciente_otras_espec','SRA_paciente_COVID19_enf_cronica','es_trabajador_IMSS','SRA_paciente_con_prueba_lab','SRA_estado_prueba_lab','SRA_CIE10_DX','pac_correo_electronico','fecha_carga']
print(df.head() )
print("contador",df.count() )
print("numero de columnas",len(df.columns ))



#df.to_csv('test2.csv', sep='^', index=False)
#os.rename(r'test2.csv',r'part-r-00000')


#hdfs.put('part-r-00000', path_tgt+'part-r-00000_migue_test')

#print(hdfs.ls(path_tgt))
#print(df.info())
#print(df.info())
if df.info():
	



"""