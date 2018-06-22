# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:35:14 2018

@author: Ayushi
"""


import numpy as np
#read csv
import pandas as pd
df = pd.read_csv("stats_females.csv")

features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

#splitting the dataset
from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


#fitting multiple regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(features_train,labels_train)

#predicting the test set result

labels_pred = regressor.predict(features_test)

#getting score for multiple value regressor model

score = regressor.score(features_test,labels_test)

#Building the optimal model using backward elimination

import statsmodels.formula.api as sm

features = np.append(arr = np.ones((214,1)).astype(int),values = features,axis=1)

features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()
#regressor_OLS.params
print('when dad height is constant then increase in avg student height is: ', regressor_OLS.params[1])

print('when Mom height is constant then increase in avg student height is: ', regressor_OLS.params[2])