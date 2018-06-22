# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 12:06:02 2018

@author: Ayushi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:22:24 2018

@author: Ayushi
"""

import pandas as pd
import numpy as np

#read file
df=pd.read_csv("affairs.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1:].values

#OneHot Encoding

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(categorical_features=[-2])
features =encoder.fit_transform(features).toarray()

features=features[:,1:]

encoder1 = OneHotEncoder(categorical_features=[-1])
features =encoder.fit_transform(features).toarray()

features=features[:,1:]


#splitting the dataset into training and testing set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,lebels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


#fittig KNN to training set
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=11,p=2)
knn.fit(features_train,labels_train)

pred = knn.predict(features_test)

#Making the confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(lebels_test,pred)

score = knn.score(features_test,lebels_test)

print("Accuracy of the model is: ",score*100,"%")

