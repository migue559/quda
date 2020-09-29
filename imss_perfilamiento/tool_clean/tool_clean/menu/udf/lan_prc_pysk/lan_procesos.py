import os,sys
from subprocess import Popen, PIPE

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def log_imprime(proc_py):
	while True:
		output = proc_py.stdout.readline()
		if output == b'' and proc_py.poll() is not None:
			break
		if output:
			print (output.strip())
	rc = proc_py.poll()
	
	return True


def lan_prc_pyspark(resultado):
    
    

    cmd = resultado.cmd_pyspark
    script = resultado.scp_pyspark
    args = resultado.par_pyspark
    print("lan_prc_pyspark", cmd, script, resultado.par_pyspark)

    try:
        pro_pyspark = Popen([cmd, script,args], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        logging.info("\t Processing >>>>>> ")
        (child_stdin, child_stdout, child_stderr) = (pro_pyspark.stdin, pro_pyspark.stdout, pro_pyspark.stderr)
        log_imprime(pro_pyspark)
        result , error = pro_pyspark.communicate()
        if pro_pyspark.returncode == 1:
            logging.info("\t Executed  with Error >>>>>> "+ str(error))
        elif pro_pyspark.returncode == 0:
            logging.info("\t Executed  succeeded >>>>>> ")

    except Exception as e:
        sys.stderr.write("common::main() : [ERROR]: output = %s" % (e))

    return True
    """
    #script='/home/miguel/tool_clean/menu/udf/lan_prc_pysk/trn_arc_con_pysk.py'
    if 1==1:
	#try:		
		process_py = Popen([cmd, script,arg ], stdin=PIPE, stdout=PIPE, stderr=PIPE)		
		logging.info("\t Processing >>>>>> ")
		(child_stdin, child_stdout, child_stderr) = (process_py.stdin, process_py.stdout, process_py.stderr)
		lan_prc_pys_log_imprime(process_py)
		result , error = process_py.communicate()
		logging.info("\t Executed  with Error >>>>>> "+ str(error))
		if process_py.returncode == 1:
			logging.info("\t Executed  with Error >>>>>> "+ str(error))
		elif process_py.returncode == 0:
			logging.info("\t Executed  succeeded >>>>>> ")
	#except Exception as e:
	#	sys.stderr.write(
	#		"common::main() : [ERROR]: output = %s" % (e))

    """	


"""
class Log(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, id=0,script='',argument='',starttime='',statusProcess='',endtime='',error=''):
        self.id   =  id
        self.script  =  script
        self.argument     =  argument
        self.starttime   =  starttime
        self.statusProcess =  statusProcess
        self.endtime       =  endtime
        self.error     =  error
               
    def Log_dic(self):    
        return {'id'            : self.id,
                'script'        : self.script,
                'argument'    : self.argument,
                'starttime'  : self.starttime,
                'statusProcess' : self.statusProcess,
                'endtime'      : self.endtime,      
                'error'    : self.error        
               }
def lan_prc_pyspark(resultado):
	print(lan_prc_pyspark"")
	return True
          

def lan_prc_pyspark(resultado ):
	print("lan_prc_pyspark")
	return True    
    cmd   ='spark-submit'
    script='/home/miguel/pruebas/trn_arc_con_pysk.py'
    try:
        process_py = Popen([cmd, script ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        logging.info("\t Processing >>>>>> ")
        (child_stdin, child_stdout, child_stderr) = (process_py.stdin, process_py.stdout, process_py.stderr)    
        print((child_stdin, child_stdout, child_stderr) )
        lan_prc_pys_log_imprime(process_py)
        result , error = process_py.communicate()
        if process_py.returncode == 1:
            logging.info("\t Executed  with Error >>>>>> "+ error)
            #break
        elif process_py.returncode == 0:
            logging.info("\t Executed  succeeded >>>>>> ")
    except Exception as e:
        sys.stderr.write(
        "common::main() : [ERROR]: output = %s" % (e))  
        #break
    return resultado
    


def lanzador_lista_procesos(lst_procesos,args=None):
    for index_value ,name_script in enumerate(lst_procesos):
        try:
            process_py = Popen([['python', 'py/' + name_script['name'] ], args ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            logging.info("\t Processing >>>>>> ")
            (child_stdin, child_stdout, child_stderr) = (process_py.stdin, process_py.stdout, process_py.stderr)    
            print((child_stdin, child_stdout, child_stderr) )
            lan_prc_pys_log_imprime(process_py)
            result , error = process_py.communicate()
            if process_py.returncode == 1:
                logging.info("\t Executed  with Error >>>>>> "+ error)
                break
            elif process_py.returncode == 0:
                logging.info("\t Executed  succeeded >>>>>> ")
        except Exception as e:
            sys.stderr.write(
            "common::main() : [ERROR]: output = %s" % (e))      
            break


def lan_prc_pys_log_imprime(process_py):
    print("rc")
    while True:
        output = process_py.stdout.readline()
        if output == b'' and process_py.poll() is not None:
            break
        if output:
            print (output.strip())
    rc = process_py.poll()
    print(rc)
    return True




if __name__ == '__main__':
    cmd   ='spark-submit'
    script='/home/miguel/pruebas/test_read_hdfs.py'
    #arg = sys.argv[1:]  
    arg=[]
    arg.append(cmd)
    arg.append(script)
    #listScripts = list_scriptsProces(arg[0])   
    print("arg",arg)
    print("Log class",Log())
    print("Log class",Log().Log_dic())
    proceso={"cmd":cmd, "script":script}

    
    lan_prc_pyspark(proceso['cmd']   ,proceso['script'])        
    

    #lista_procesos=[]
    #lista_procesos.append(proceso)
    #lista_procesos.append(proceso)
    #lanzador_lista_procesos(cmd,script)        
    

"""
            
