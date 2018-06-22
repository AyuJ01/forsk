# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:54:25 2018

@author: Ayushi
"""

import glob
import numpy as np
import matplotlib.pyplot as plt
import os

listoffolders=os.listdir("E:\\data science\\datasets\\mnist\\mnist_png\\training")

#for SubFolder in listoffolders:
SubFolder=0
ListofImages=os.listdir("E:\\data science\\datasets\\mnist\\mnist_png\\training\\"+str(SubFolder))

print(ListofImages)

S=(plt.imread("E:\\data science\\datasets\\mnist\\mnist_png\\training\\"+str(0)+"\\"+"1.png")).shape
MeanImages=[]

for SubFolder in listoffolders:
    Sum=np.zeros([S[0],S[1]])
    ListofImages=os.listdir("E:\\data science\\datasets\\mnist\\mnist_png\\training\\"+str(SubFolder))
    
    for Image in ListofImages:
        Sum+=plt.imread("E:\\data science\\datasets\\mnist\\mnist_png\\training\\"+str(SubFolder)+"\\"+Image)

    
Sum=Sum/len(ListofImages)
MeanImages.append(Sum)
plt.imshow(MeanImages[0])
plt.show()
    



for SubFolder in listoffolders:
    Sum=np.zeros([S[0],S[1]])
    ListofImages=os.listdir("E:\\data science\\datasets\\mnist\\mnist_png\\training\\"+str(SubFolder))
    
    for Image in ListofImages:
        Sum+=plt.imread("E:\\data science\\datasets\\mnist\\mnist_png\\training\\"+str(SubFolder)+"\\"+Image)
    
Sum=Sum/len(ListofImages)
MeanImages.append(Sum)
plt.imshow(MeanImages[0])
plt.show()
    
