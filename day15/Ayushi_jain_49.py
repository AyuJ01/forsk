# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:52:56 2018

@author: Ayushi
"""

import pandas as pd

#Read csv
df = pd.read_csv("Red_Wine.csv",sep = ',')

#taking care of missing data
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])


#split into features and labels
features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

#Encoding the categorical data
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
labelencoder = LabelEncoder()

features[:,0] = labelencoder.fit_transform(features[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])

features = onehotencoder.fit_transform(features).toarray()



#Split the data set into training and test set

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#features scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


