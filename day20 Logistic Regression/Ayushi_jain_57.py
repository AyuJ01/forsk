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


#fitting Logistic regression into training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(features_train,labels_train)

#predicting the test set Result
labels_pred = classifier.predict(features_test)

#claculate the score
score = classifier.score(features_test,lebels_test)

#making the confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lebels_test,labels_pred)

#percentage of affair
affair = df["affair"].value_counts(normalize=True)*100

#predict random result
pred_affair = classifier.predict_proba(np.array([1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,16]).reshape(1,-1))
aff = list(pred_affair[0])

max_prob = max(aff)
index = aff.index(max_prob)

print("percentage of total women actually had an affair is : ", affair[1])
print("Prediction of women : ",index)


#optimal Model
import statsmodels.formula.api as sm

features = np.append(arr = np.ones((6366,1)).astype(int),values = features,axis=1)

features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,6,7,8,9,10,11,12,13,14,15,16]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,6,7,8,9,10,11,12,13,14,15]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,6,7,8,9,10,11,12,13,15]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,11,12,13,15]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()


#We observe that  children,education,occupation & occupation_husb columns are not impotant 

#before One Hot Encoding

features = df.iloc[:,:-1].values

features_opt = features[:,[0,1,2,3,4,5,6,7,8]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:,[0,1,2,3,5,6,7,8]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:,[0,1,2,3,5,6,7]]
regressor_OLS = sm.OLS(endog=labels,exog = features_opt).fit()
regressor_OLS.summary()

#We observe that  children & occupation_husb columns are not impotant 
