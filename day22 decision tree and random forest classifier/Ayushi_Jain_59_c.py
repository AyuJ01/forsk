# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:12:06 2018

@author: Ayushi
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tree_addhealth.csv")

for i in df:
    df[i] = df[i].fillna(df[i].mode()[0]) 

features = df.iloc[:,1:6].values
labels = df.iloc[:,7].values



#split into training set and testing set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#fitting random forest Classifier to the training set
from sklearn.ensemble import RandomForestClassifier as rf
classifier = rf(n_estimators = 10,criterion = 'entropy',random_state = 0)

classifier.fit(features_train,labels_train)

#predicting the test set results

labels_pred = classifier.predict(features_test)

score = classifier.score(features_test,labels_test)

#making the confusion matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test,labels_pred)

