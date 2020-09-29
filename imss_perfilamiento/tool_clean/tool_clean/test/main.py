from test.obj_clases import Archivo,LogProcesos,Menu
from test.menu import menu_general



if __name__ == '__main__':
    # arg = sys.argv[1:]
    arg = []
    # listScripts = list_scriptsProces(arg[0])
    dic_menu = {'opc_1': 2, 'opc_2': 1}
    archivo_1 = Archivo(1, 'part-m-00000', '^', True)

    ruta_src = '/dev/la/la_nssa/CAT_UMF/'
    ruta_tgt = '/dev/la/lt_nssa/CAT_UMF/'

    lis_menu = [archivo_1]
    #menu = Menu(id_menu=1, argumentos_menu=dic_menu, archivos=lis_menu, ruta_src=ruta_src, ruta_tgt=ruta_tgt)

    log_procesos = LogProcesos()
    print('hola')

  #  menu_general(menu)


