import os,sys,json
from types import SimpleNamespace

def recoverValue(dictionary,key_search):
	for key, value in dictionary.items():
		if key == key_search:
			return value

def GetData(file=None):
	try:
		with open('menu/cfg/{file}'.format(file=file)) as json_file:  
			data = json.load(json_file)
	except Exception as e:
		with open('{file}'.format(file=file)) as json_file:  
			data = json.load(json_file)
	return data

def GetDataConnections():
	return recoverValue(GetData(), 'Connections')

def cfg_obt_dato_reglas():
	return recoverValue(GetData('reglas.json'), 'Reglas')

def cfg_obt_par_pyspark(file):
	return GetData(file)

reglas = cfg_obt_dato_reglas()
