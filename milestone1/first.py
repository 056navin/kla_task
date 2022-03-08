import yaml
from yaml.loader import SafeLoader
from datetime import datetime
import time
import threading
 
a_yaml_file = open("Milestone1B.yaml")
workflow= yaml.load(a_yaml_file, Loader=yaml.SafeLoader)

file = open("log2.txt","w")
threads= []
def flow(work, execution, activities):
    if execution == "sequential":
        for act in activities:
            now = datetime.now()
            file.write(f"{now};{work}.{act} Entry\n")
            if activities[act]['Type'] == "Flow":
                newwork = work + '.' + act
                flow(newwork,activities[act]['Execution'],activities[act]['Activities'])
            elif activities[act]['Type'] == "Task":
                newwork = work + '.' + act
                task(newwork,activities[act]['function'],activities[act]['Inputs'])
            now= datetime.now()
            file.write(f"{now};{work}.{act} Exit\n")
    if execution == "Concurrent":
        for act in activities:
            now = datetime.now()
            file.write(f"{now};{work}.{act} Entry\n")
            if activities[act]['Type'] == "Flow":
                newwork = work + '.' + act 
                thread = threading.Thread(target=flow,args=[newwork,activities[act]['Execution'],activities[act]['Activities']])
                thread.start()
                thread.append({thread,newwork})
            elif  activities[act]['Type'] == "Task":
                newwork = work + '.' + act
                thread = threading.Thread(target=task,args=[newwork,activities[act]['Function'],activities[act]['Inputs']])  
                thread.start()
                thread.append({thread,newwork}) 
            now = datetime.now()
            for thread in threads:
                thread.join()
            file.write(f"{now};{work}.{act} Exit\n")
    def task(work,function,inputs):
        if function == 'TimeFunction':
          fun_input = inputs['FunctionInput']  
          exc_time =inputs['ExecutionTime']
        now = datetime.now()
        file.write(f"{now};{work} Executing {function} ({fun_input}), {exc_time})\n")
        time.sleep(int(exc_time))
for work in workflow:
        now = datetime.now()
        file.write(F"{now};{work} Entry\n")
        if workflow[work]['Type'] == "flow":
            flow(work,workflow[work]['Execution'],workflow[work]['Activities'])
        elif workflow[work]['Type'] == "Task":
            task(work,workflow[work]['function'],workflow[work]['Inputs'])   
        now = datetime.now()
        file.write(f"{now};{work} Exit")    