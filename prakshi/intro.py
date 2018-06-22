# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:14:32 2018

@author: tanmay
"""
import numpy as np
x=np.array([[1,2],[3,4]],np.int32)
type(x)
'''if data type not given den int16'''
x=np.array([[1,2],[3,4]])

x=np.float32(1.0)
print(x)

y=np.int_([1,2,3])
#converting python tuple and list to nd array
x=np.array([2,3,1])
print(x)

x=np.array((1,2,3))
print(x)

x=np.linspace(1.,4.,10)
incomes=np.random.normal(27000,15000,10000) #(avg value,std deviation,no of people)
import matplotlib.pyplot as plt
plt.hist(incomes,20)
plt.show()

np.median(incomes)
np.mean(incomes)
incomes=np.append(incomes,[10000000000000])#the list is outlier