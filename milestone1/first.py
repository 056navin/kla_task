import yaml
from yaml.loader import SafeLoader
from datetime import datetime 
import time
import threading
 
a_yaml_file = open("Milestone1A.yaml")
workflow= yaml.load(a_yaml_file, Loader=yaml.SafeLoader)

file = open("log1.txt","w")
threads= []
def flow(ob, execution, activities):
    if execution == "Sequential":
        for n in activities:
            now = datetime.now()
            file.write(f"{now};{ob}.{n} Entry\n")
            if activities[n]['Type'] == "Flow":
                newwork = ob + '.' + n
                flow(newwork,activities[n]['Execution'],activities[n]['Activities'])
            elif activities[n]['Type'] == "Task":
                newwork = ob + '.' + n
                task(newwork,activities[n]['Function'],activities[n]['Inputs'])
            now= datetime.now()
            file.write(f"{now};{ob}.{n} Exit\n")
def task(ob,function,inputs):
        if function == 'TimeFunction':
            fun_input = inputs['FunctionInput']  
            exc_time =inputs['ExecutionTime']
        now = datetime.now()
        file.write(f"{now};{ob} Executing {function} ({fun_input}), {exc_time})\n")
        time.sleep(int(exc_time))
for ob in workflow:
        now = datetime.now()
        file.write(F"{now};{ob} Entry\n")
        if workflow[ob]['Type'] == "Flow":
            flow(ob,workflow[ob]['Execution'],workflow[ob]['Activities'])
        elif workflow[ob]['Type'] == "Task":
            task(ob,workflow[ob]['function'],workflow[ob]['Inputs'])   
        now = datetime.now()
        file.write(f"{now};{ob} Exit")     