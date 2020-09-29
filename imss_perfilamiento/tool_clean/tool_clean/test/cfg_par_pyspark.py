import os,sys,json
from types import SimpleNamespace


def GetData(file=None):
	try:
		with open('menu/cfg/{file}'.format(file=file)) as json_file:  
			data = json.load(json_file)
	except Exception as e:
		with open('{file}'.format(file=file)) as json_file:  
			data = json.load(json_file)
	return data

def cfg_obt_par_pyspark(file):
	return GetData(file)



