# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:03:38 2018

@author: Ayushi
"""

#read csv
import pandas as pd
df = pd.read_csv("PastHires.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1:].values

#label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,3] = labelencoder.fit_transform(features[:,3])
features[:,4] = labelencoder.fit_transform(features[:,4])
features[:,5] = labelencoder.fit_transform(features[:,5])

labels[:,-1] = labelencoder.fit_transform(labels[:,-1])

#fitting decision tree regressor to dataset

from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features,labels)




#fitting random forest regression 
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=10,random_state=0)
reg.fit(features,labels)


#predicting the result
import numpy as np
pred1 = regressor.predict(np.array([10,1,4,0,1,0]).reshape(1,-1))

pred2 = reg.predict(np.array([10,1,4,0,1,0]).reshape(1,-1))

pred3 = regressor.predict(np.array([10,0,4,1,0,1]).reshape(1,-1))

pred4 = reg.predict(np.array([10,0,4,1,0,1]).reshape(1,-1))


