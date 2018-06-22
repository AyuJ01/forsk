# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:14:37 2018

@author: Ayushi
"""
#import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("breast_cancer.csv")

#Handling missing values
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])
    
    
features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1].values

#splitting the dataset
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#Fitting SVM to training set
from sklearn.svm import SVC
classifier = SVC(kernel = "linear", random_state=0)
classifier.fit(features_train,labels_train)

#predict the test set results
pred = classifier.predict(features_test)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,pred)

#Calculating the score
score = classifier.score(features_test,labels_test)

pred_cancer = classifier.predict(np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1))


#PCA principle component Analysis
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

 
#Fitting SVM to training set
from sklearn.svm import SVC
classifier1 = SVC(kernel = "linear", random_state=0)
classifier1.fit(features_train,labels_train)



# Visualising the Test set results
from matplotlib.colors import ListedColormap
features_set, labels_set = features_test, labels_test
X1, X2 = np.meshgrid(np.arange(start = features_set[:, 0].min() - 1, stop = features_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = features_set[:, 1].min() - 1, stop = features_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier1.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('green','red')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
                c = ListedColormap(('green','red'))(i), label = j)
plt.title('SVM (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()