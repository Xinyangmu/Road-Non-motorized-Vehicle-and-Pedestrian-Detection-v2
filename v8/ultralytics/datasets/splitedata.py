import os,glob,shutil
import numpy as np

from ultralytics.datasets.data_config import get_train_data

allfi = glob.glob(os.path.join(get_train_data(),"traindata","*.png"))
np.random.shuffle(allfi)
k = 0
for file in allfi:
    if k < len(allfi) *0.2:
        target = file.replace("traindata","valdata")
        shutil.move(file.replace(".png",".txt"),target.replace(".png",".txt"))
        shutil.move(file,target)
    k+=1
