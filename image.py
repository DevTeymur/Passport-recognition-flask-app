import keras
import numpy as np
from keras.preprocessing import image
from os import listdir
from os.path import isfile, join
import pandas as pd
from sklearn.metrics import classification_report
from warnings import filterwarnings
filterwarnings("ignore")
import os



def returnArray(imgPath, size = 200):

    img = image.load_img(imgPath, target_size=(size, size), grayscale=False)
    resized_img = image.img_to_array(img)
    return np.array(resized_img).reshape(1, size, size, 3)

def returnImgCls(imgName, size = 200):
    
    imgPath=mypath+"/test_images/"+imgName
    
    # imgPath=imgName

    d={1:"Front Face",2:"Back Face",3:"None"}
    
    img = returnArray(imgPath)

    res=d[clsRes(img)[0]]
    
    return res +"  |  "+imgName