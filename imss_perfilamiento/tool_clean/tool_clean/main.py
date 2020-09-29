# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from menu.obj.obj_clases import Menu, Archivo, Proceso, LogProcesos
from menu.menu import menu_general


if __name__ == '__main__':
    # arg = sys.argv[1:]
    arg = []
    # listScripts = list_scriptsProces(arg[0])
    dic_menu = {'opc_1': 1, 'opc_2': 1}
    archivo_1 = Archivo(1, 'UMF_test.txt', '^', True)
    
    
    #ruta='C:/Users/miguel.cruza/PycharmProjects/tool_clean/'
    ruta_src='C:/Users/othon.suarez/Documents/hdfs/'
    ruta_tgt='C:/Users/othon.suarez/Documents/hdfs/'


    lis_menu = [archivo_1]
    #menu = Menu(id_menu=1, argumentos_menu=dic_menu, archivos='*',ruta=ruta, separador='^', encabezado=True)
    menu = Menu(id_menu=1, argumentos_menu=dic_menu, archivos=lis_menu,ruta_src=ruta_src, ruta_tgt=ruta_tgt)

    log_procesos = LogProcesos()

    
    menu_general(menu)
