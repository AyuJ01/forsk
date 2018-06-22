# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:02:09 2018

@author: Ayushi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:21:21 2018

@author: Ayushi
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("tree_addhealth.csv")

for i in df1:
    df1[i] = df1[i].fillna(df1[i].mode()[0]) 

df = df1[["BIO_SEX","VIOL1","EXPEL1"]]
features = df.iloc[:,0:2].values
labels = df.iloc[:,-1].values



#split into training set and testing set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)



#fitting decision tree regressor to dataset

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy',random_state=0)
classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

score = classifier.score(features_test,labels_test)

#making the confusion matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test,labels_pred)

