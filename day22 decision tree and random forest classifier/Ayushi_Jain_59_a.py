# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:21:21 2018

@author: Ayushi
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tree_addhealth.csv")

for i in df:
    df[i] = df[i].fillna(df[i].mode()[0]) 

features = df.iloc[:,:-9]
labels = features.iloc[:,7:8].values

features = features.drop(df.columns[7], axis=1)
features = features.iloc[:,:].values


#split into training set and testing set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


#features scaling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#fitting decision tree classifier to dataset

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy',random_state=0)
classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

score = classifier.score(features_test,labels_test)

#making the confusion matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test,labels_pred)

