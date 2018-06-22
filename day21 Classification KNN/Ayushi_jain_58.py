# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:59:33 2018

@author: Ayushi
"""

#import libraries
import pandas as pd

df_o = pd.read_csv("mushrooms.csv")
df = df_o.iloc[:,[0,5,-2,-1]]

#handle Categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

df["class"] = labelencoder.fit_transform(df["class"])


df = pd.get_dummies(df, columns=['odor'])
df = df.drop(df.columns[-1], axis=1)

df = pd.get_dummies(df, columns=['population'])
df = df.drop(df.columns[-1], axis=1)

df = pd.get_dummies(df, columns=['habitat'])
df = df.drop(df.columns[-1], axis=1)

features = df.iloc[:,1:].values
labels = df.iloc[:,0:1].values

#spliting the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,lebels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#fittig KNN to training set
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5,p=2)
knn.fit(features_train,labels_train)

pred = knn.predict(features_test)

#Making the confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(lebels_test,pred)

score = knn.score(features_test,lebels_test)

print("Accuracy of the model is: ",score*100,"%")

