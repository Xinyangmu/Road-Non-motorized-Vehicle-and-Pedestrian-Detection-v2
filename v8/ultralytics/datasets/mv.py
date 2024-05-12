import os,glob,shutil
import numpy as np

from ultralytics.datasets.data_config import get_train_data

# 0: pedestrian
# 1: people
# 2: bicycle
# 3: car
# 4: van
# 5: truck
# 6: tricycle
# 7: awning - tricycle
# 8: bus
# 9: motor


for fold in ["traindata","valdata","testdata"]:
    allfi = glob.glob(os.path.join(get_train_data(),fold,"labels","*.txt"))
    for file in allfi:
        name = file.split(os.sep)[-1].split(".")[0]
        targetlines = []
        with open(file,"r") as f:
            for line in f.readlines():
                info = line.split(" ")
                if int(info[0]) ==0 or int(info[0]) ==1:
                    info[0] = "0"
                    targetlines.append(info)
                elif  int(info[0]) ==2:
                    info[0] = "1"
                    targetlines.append(info)
        if len(targetlines) >=0 :
            with open(os.path.join(get_train_data(),fold,f"{name}.txt"),"w") as f:
                for info in targetlines:
                    f.write(" ".join(info))
            shutil.copy(file.replace("labels","images").replace(".txt",".jpg"),
                        os.path.join(get_train_data(), fold, f"{name}.jpg"))
            #print("====")

