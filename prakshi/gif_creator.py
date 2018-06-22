# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:12:24 2018

@author: tanmay
"""
#convert images into gif

import imageio
images = []
files=['img1.png','img2.jpg','img3.jpg']

for filename in files:
    images.append(imageio.imread(filename))
imageio.mimsave('first.gif',images,duration=0.5)    
 
#%%
#convert video into gif

 #split video into frames
import cv2
vidcap = cv2.VideoCapture('../mrng.mp4')
count = 0 
success,image = vidcap.read()
while success:
    success,image = vidcap.read()
    cv2.imwrite("frame%d.jpg" % count, image)
    if cv2.waitKey(10) == 27:
         break
    count += 1
    

#merge frames
import os ,imageio as io
ls =[]
a = os.listdir(os.getcwd())
for filename in sorted(a):
    ls.append(filename)
images = []
for filename in ls:
    images.append(io.imread(filename))
io.mimsave('surface1.gif', images, duration = 0.005)
