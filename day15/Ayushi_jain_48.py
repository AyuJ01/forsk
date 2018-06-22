# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:19:57 2018

@author: Ayushi
"""

import pandas as pd
#import the csv and name the missing columns name
df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None,
     usecols=[0,1,2],
     sep = ',',
     names=['Class label', 'Alcohol', 'Malic acid']
    )

#split the data

from sklearn.model_selection import train_test_split

features = df.iloc[:,1:3].values
labels = df.iloc[:,0].values

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.2,random_state = 0)

"""
#feature scaling  // standard scaler
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train = sc.fit_transform(features_train)

features_test = sc.transform(features_test)
"""

#Min-max scaling
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler()

features_train = sc.fit_transform(features_train)

features_test = sc.transform(features_test)



