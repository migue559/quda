import os,sys

def limpia_pantalla():
	try:
		sys.stderr.write("\x1b[2J\x1b[H")
	except Exception as e:
		os.system("cls")


