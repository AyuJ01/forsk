# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:26:07 2018

@author: Ayushi
"""

#read csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("Bahubali2_vs_Dangal.csv")

features = df.iloc[:,0:1].values
label1 = df.iloc[:,1:2].values
label2 = df.iloc[:,2:].values

#predict for bahubali2
#splitting the data

features_train1,features_test1,labels_train1,labels_test1 = train_test_split(features,label1,test_size=0.2,random_state=0)

#fitting the linear regression to training set

regressor = LinearRegression()

regressor.fit(features_train1,labels_train1)

#predicting the test result

label1_predict = regressor.predict(features_test1)

#Model score
score = regressor.score(features_test1,labels_test1)


#Visulaizing the training set result

plt.scatter(features_train1,labels_train1,color='red')
plt.plot(features_train1,regressor.predict(features_train1),color='blue')

plt.title("day v/s collections of Bahubali-2 graph")
plt.xlabel("Day")
plt.ylabel("Collections")

plt.show()
plt.close()

#predict the 10th day collections of balubali2

bahu_10 = regressor.predict(10)
print("10th day collections of bahubali-2 in crore is : ",bahu_10)



#predict for dangal
#splitting the data

features_train2,features_test2,labels_train2,labels_test2 = train_test_split(features,label2,test_size=0.2,random_state=0)

#fitting the linear regression to training set

regressor2 = LinearRegression()

regressor2.fit(features_train2,labels_train2)

#predicting the test result

label2_predict = regressor2.predict(features_test2)

#Model score
score = regressor2.score(features_test2,labels_test2)


#Visulaizing the training set result

plt.scatter(features_train2,labels_train2,color='green')
plt.plot(features_train2,regressor2.predict(features_train2),color='yellow')

plt.title("day v/s collections of Dangal graph")
plt.xlabel("Day")
plt.ylabel("Collections")

plt.show()
plt.close()
#predict the 10th day collections of balubali2

dangal_10 = regressor2.predict(10)
print("10th day collections of dangal in crore is : ",dangal_10)


plt.plot(features,label1,color='green',label="Bahubali 2")
plt.plot(features,label2,color='red', label="Dangal")
plt.scatter(10,regressor.predict(10),color='green')
plt.scatter(10,regressor2.predict(10),color='red')
plt.title("day v/s collections of Dangal graph")
plt.xlabel("Day")
plt.ylabel("Collections")
plt.legend()
plt.show()

