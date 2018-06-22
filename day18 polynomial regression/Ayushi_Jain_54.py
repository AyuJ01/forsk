# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:28:36 2018

@author: Ayushi
"""

#read csv
import pandas as pd
df = pd.read_csv("bluegills.csv")

labels = df.iloc[:,1:].values
features = df.iloc[:,0:1].values

#fitting the linear regression to the dataset
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

#visualsing the linear Regression Result

import matplotlib.pyplot as plt

plt.scatter(features,labels,color='red')

plt.plot(features,regressor.predict(features),color='blue')

plt.show()

#fitting polynomial regressor to dataset
from sklearn.preprocessing import PolynomialFeatures

poln_object = PolynomialFeatures(degree=2)

features_poln = poln_object.fit_transform(features) 

regressor_2 = LinearRegression()
regressor_2.fit(features_poln,labels)

#visualizing the Polynomial regression Result

plt.scatter(features,labels,color='red')
plt.plot(features,regressor_2.predict(poln_object.fit_transform(features)),color='blue')
plt.show()


#visualizing the Polynomial regression Result (for higher resolution and smoother curve
import numpy as np
features_grid = np.arange(min(features),max(features),0.1)
features_grid = features_grid.reshape((-1,1))

plt.scatter(features,labels,color='red')
plt.plot(features_grid,regressor_2.predict(poln_object.fit_transform(features_grid)),color='blue')
plt.show()


print("predicted length of five-year-old bluegill fish is : ")
print(regressor_2.predict(poln_object.fit_transform(5)))
