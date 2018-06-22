# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:08:25 2018

@author: tanmay
"""

import numpy as np
n=input()  #n=input().strip().split(' ')
n.strip()
l=n.split(' ')

m=list(map(int,l))
arr=np.asarray(m)#convert list into ndarray
a=arr.reshape(3,3) #to reshape in 3 rows and 3 cols
print(a)