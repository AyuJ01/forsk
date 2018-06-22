# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:10:53 2018

@author: Ayushi
"""

#import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read csv
df = pd.read_csv("crime_data.csv")
X = df.iloc[:,[1,2,4]].values

"""
#features Scaling 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
"""

#PCA principle component Analysis
from sklearn.decomposition import PCA
"""
#explains the value of n_components
///only with high explained_variance are used

pca = PCA(n_components=None)
X = pca.fit_transform(X)
explained_variance = pca.explained_variance_ratio_
"""


pca = PCA(n_components=2)
X = pca.fit_transform(X)
explained_variance = pca.explained_variance_ratio_


#using the elbow method to find the optimal no. of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++',random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title("The Elbow Method")
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#fitting K-Means to the dataset with 4 clusters
kmeans = KMeans(n_clusters = 3,init = 'k-means++',random_state= 0)
y_kmeans = kmeans.fit_predict(X)

#Visulaing the clusters
plt.scatter(X[y_kmeans == 0,0],X[y_kmeans == 0,1],s = 100, c = 'red',label = 'Murder')
plt.scatter(X[y_kmeans == 1,0],X[y_kmeans == 1,1],s = 100, c = 'blue',label = 'Assault')
plt.scatter(X[y_kmeans == 2,0],X[y_kmeans == 2,1],s = 100, c = 'green',label = 'Rape')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300, c = 'yellow',label='Centroids')
plt.title("clusters of Crime")
plt.xlabel('pc1')
plt.ylabel('pc2')

plt.legend()
plt.show()
