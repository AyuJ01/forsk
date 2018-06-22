# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:46:41 2018

@author: tanmay
"""

import pandas as pd
df=pd.read_csv("Automobile.csv")
A=[]
a=df['make'].value_counts()
A = list(a)
b = list(a.index) #to extract labels or names of cars

import matplotlib.pyplot as plt
labels=b[0:10]
sizes=A[0:10]
exp=[0.2,0,0,0,0,0,0,0,0,0]
ax1 = plt.subplot()
ax1.pie(sizes, labels=labels, autopct='%1.2f%%',explode=exp)
ax1.show()
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.