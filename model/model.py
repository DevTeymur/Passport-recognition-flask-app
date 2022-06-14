import keras
import numpy as np
from keras.preprocessing import image
from os import listdir
from os.path import isfile, join
import pandas as pd
from sklearn.metrics import classification_report
import sys
sys.path.append("./")
from warnings import filterwarnings
filterwarnings("ignore")
import os

# mypath="C:/Users/UFAZ/Desktop/work/Germancy/model" # path
mypath="/mnt/c/Users/UFAZ/Desktop/work/Germancy/final/Passport-recognition-flask-app/"
model1 = keras.models.load_model(mypath+'model/my_model.h5')

def returnArray(imgPath, size = 200):

    img = keras.utils.load_img(mypath+"static/uploads/"+imgPath, target_size=(size, size), grayscale=False)
    # load_img('path_to_image', target_size=(img_size, img_size))
    resized_img = keras.utils.img_to_array(img)
    return np.array(resized_img).reshape(1, size, size, 3)

def clsRes(imgArr):
    y_pred=np.around(model1.predict(imgArr),decimals=3)
    y_pred=list(y_pred[0])
    index=y_pred.index(max(y_pred))
    return index+1,y_pred


# Function to be used in main.py
def returnImgCls(imgName, size = 200):
    # imgPath=mypath+"/test_images/"+imgName
    imgPath=imgName
    d={1:"Front Face",2:"Back Face",3:"None"}
    img = returnArray(imgPath)
    res=d[clsRes(img)[0]]
    return res +"  |  "+imgName

















