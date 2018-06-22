# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:25:39 2018

@author: tanmay
"""
import pandas as pd
df=pd.read_csv("cars.csv")
X = df.iloc[:,1:].values
y = df.iloc[:,0].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
df1=pd.DataFrame(X_train)
df2=pd.DataFrame(X_test)
df3=pd.DataFrame(y_train,columns=["y_train"])
df4=pd.DataFrame(y_test,columns=["y_test"])
df1.to_csv("X_train.csv",index=False)
df2.to_csv("X_test.csv",index=False)
df3.to_csv("y_train.csv",index=False)
df4.to_csv("y_test.csv",index=False)