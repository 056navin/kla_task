import yaml
from yaml.loader import SafeLoader
from datetime import datetime 
import time
import threading
 
a_yaml_file = open("Milestone1B.yaml")
workflow= yaml.load(a_yaml_file, Loader=yaml.SafeLoader)

file = open("log2.txt","w")
threads= []
def flow(obj, execution, activities):
    if execution == "sequential":
        for n in activities:
            now = datetime.now()
            file.write(f"{now};{obj}.{n} Entry\n")
            if activities[n]['Type'] == "Flow":
                newwork = obj + '.' + n
                flow(newwork,activities[n]['Execution'],activities[n]['Activities'])
            elif activities[n]['Type'] == "Task":
                newwork = obj + '.' + n
                task(newwork,activities[n]['function'],activities[n]['Inputs'])
            now= datetime.now()
            file.write(f"{now};{obj}.{n} Exit\n")
    if execution == "Concurrent":
        for n in activities:
            now = datetime.now()
            file.write(f"{now};{obj}.{n} Entry\n")
            if activities[n]['Type'] == "Flow":
                newobj = obj + '.' + n 
                thread = threading.Thread(target=flow,args=[newwork,activities[n]['Execution'],activities[n]['Activities']])
                thread.start()
                thread.append({thread,newwork})
            elif  activities[n]['Type'] == "Task":
                newwork = obj + '.' + n
                thread = threading.Thread(target=task,args=[newwork,activities[n]['Function'],activities[n]['Inputs']])  
                thread.start()
                thread.append({thread,newwork}) 
            now = datetime.now()
            for thread in threads:
                thread.join()
            file.write(f"{now};{obj}.{n} Exit\n")
    def task(obj,function,inputs):
        if function == 'TimeFunction':
          fun_input = inputs['FunctionInput']  
          exc_time =inputs['ExecutionTime']
        now = datetime.now()
        file.write(f"{now};{obj} Executing {function} ({fun_input}), {exc_time})\n")
        time.sleep(int(exc_time))
for obj in workflow:
        now = datetime.now()
        file.write(F"{now};{obj} Entry\n")
        if workflow[obj]['Type'] == "flow":
            flow(obj,workflow[obj]['Execution'],workflow[obj]['Activities'])
        elif workflow[obj]['Type'] == "Task":
            task(obj,workflow[obj]['function'],workflow[obj]['Inputs'])   
        now = datetime.now()
        file.write(f"{now};{obj} Exit")    