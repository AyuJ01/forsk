# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:56:40 2018

@author: Ayushi
"""

#read file
import pandas as pd

df = pd.read_csv('Auto_mpg.txt', delim_whitespace=True, header=None)

df.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]

high_mpg = max(df.iloc[:,0].values)

loc = df[df['mpg'] == 46.6].index.tolist()

car = df.iloc[322,-1]

print("car with highest mpg is : ",car)

#handle missing values
df["horsepower"][df["horsepower"]=='?'] = df["horsepower"].mode()[0]

df['horsepower'] = df['horsepower'].convert_objects(convert_numeric=True)

#split into labels and features

features = df.iloc[:,1:-1].values
labels = df.iloc[:,0:1].values

#split into training set and testing set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

"""
#Decisiion tree regressor
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features_train,labels_train)

labels_pred_1 = regressor.predict(features_test)

score_1 = regressor.score(features_test,labels_test)


#fitting random forest regression 
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=200,random_state=0)
reg.fit(features_train,labels_train)

labels_pred_2 = reg.predict(features_test)

score_2 = reg.score(features_test,labels_test)




#predicting the result
import numpy as np
pred1 = regressor.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))
pred2 = reg.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))

print("prediction from decision tree : ",pred1)
print("prediction from random forest : ",pred2)
"""

###
#features scaling
import numpy as np

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)
value = np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
value = sc.transform(value)
#Decisiion tree regressor
from sklearn.tree import DecisionTreeRegressor
regressor1 = DecisionTreeRegressor(random_state=0)
regressor1.fit(features_train,labels_train)

labels_pred_3 = regressor1.predict(features_test)

score_3 = regressor1.score(features_test,labels_test)


#fitting random forest regression 
from sklearn.ensemble import RandomForestRegressor
reg1 = RandomForestRegressor(n_estimators=200,random_state=0)
reg1.fit(features_train,labels_train)

labels_pred_4 = reg1.predict(features_test)

score_4 = reg1.score(features_test,labels_test)




#predicting the result
pred3 = regressor1.predict(value)
pred4 = reg1.predict(value)

print("prediction from decision tree : ",pred3)
print("prediction from random forest : ",pred4)





