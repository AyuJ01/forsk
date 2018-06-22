# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:34:22 2018

@author: tanmay
"""

import matplotlib.pyplot as plt
xs=[1,2,3,4]
ys=[1,2,3,4]
plt.plot(xs,ys) #straight lyn


xs=[1,2,3,4]
ys=[1,4,9,16]
plt.plot(xs,ys) #form parabola

xs=[1,2,3,4]
ys=[x**2 for x in xs]
plt.plot(xs,ys) #form parabola


plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib eg")
plt.savefig("quad.png")
plt.show()

'''dataset
-find missing values and handle
-categorical data
-labelled set(supervised ML) or unsupervised Ml
-if u see labelled data set(supervised ML) the seprate indep values[divided in(x_train and x_test)] and dep values(y_train and y_test) using pandas iloc
'''
