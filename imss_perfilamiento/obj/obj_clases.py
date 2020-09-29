class File(object):
    def __init__(self, nombre='', ext='', separador='', encabezado=False, ruta_src=''):
        self.nombre = nombre
        self.ext = ext
        self.separador = separador
        self.encabezado = encabezado
        self.ruta_src = ruta_src

class Menu(object):
    def __init__(self, id_menu=1, argumentos_menu={}, ruta_tgt='', reglas=''):
        self.id_menu = id_menu
        self.argumentos_menu = argumentos_menu
        self.ruta_tgt = ruta_tgt
        self.reglas = reglas

class Reporte(object):
    def __init__(self,id_configuracion='',archivo='',columna='',funcion='',parametro=''):
        self.id_configuracion = id_configuracion
        self.archivo = archivo
        self.columna = columna
        self.funcion = funcion
        self.parametro = parametro

class queryMongo(object):
    def __init__(self,collection='',filter={},df=''):
        self.collection = collection
        self.filter = filter
        self.df = df