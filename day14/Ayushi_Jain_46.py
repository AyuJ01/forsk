# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:00:57 2018

@author: Ayushi
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

df=pd.read_csv("Loan.csv")
df = df.drop("Loan_ID",axis=1)
X = df.iloc[:,:-1].values          #features
y = df.iloc[:,-1].values           #labels

labelencoder = LabelEncoder()

X[:,1] = labelencoder.fit_transform(X[:,1])
X[:,2] = labelencoder.fit_transform(X[:,2])
X[:,3] = labelencoder.fit_transform(X[:,3])
X[:,4] = labelencoder.fit_transform(X[:,4])
X[:,0] = labelencoder.fit_transform(X[:,0])

X[:,-1] = labelencoder.fit_transform(X[:,-1])

onehotencoder = OneHotEncoder(categorical_features=[-1])

X = onehotencoder.fit_transform(X).toarray()

y = labelencoder.fit_transform(y)


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


