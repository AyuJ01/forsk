# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:57:50 2018

@author: Ayushi
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("banknotes.csv")

features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1:].values

#features Scaling 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)


#splitting the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


#Logistic Regression  #score=95
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(features_train,labels_train)
pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,pred)

score = classifier.score(features_test,labels_test)

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




