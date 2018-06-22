# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:06:18 2018

@author: Ayushi
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Foodtruck.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

#Splitting the data
from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state = 0)

#Fitting linear regression to training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features_train,labels_train)

#predicting the test result
labels_pred = regressor.predict(features_test)

#Model score
score = regressor.score(features_test,labels_test)



#Visulaizing the training set result

plt.scatter(features_train,labels_train,color='red')
plt.plot(features_train,regressor.predict(features_train),color='blue')

plt.title("Population v/s profit graph")
plt.xlabel("Population")
plt.ylabel("profit")

plt.show()
plt.close()


#profit in jaipur
jaipur_pred = regressor.predict(3.073)
print("Profit in Jaipur : ",jaipur_pred)
