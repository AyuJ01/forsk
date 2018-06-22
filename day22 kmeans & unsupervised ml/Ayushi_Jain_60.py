# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:26:54 2018

@author: Ayushi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("deliveryfleet.csv")

features = df.iloc[:,1:3].values

#Using the elbow method to find the optimal no. of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++',random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title("The Elbow Method")
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#fitting K-Means to the dataset with 2 clusters
kmeans = KMeans(n_clusters = 2,init = 'k-means++',random_state= 0)
y_kmeans = kmeans.fit_predict(features)

#Visulaing the clusters
plt.scatter(features[y_kmeans == 0,0],features[y_kmeans == 0,1],s = 100, c = 'red',label = 'cluster 1')
plt.scatter(features[y_kmeans == 1,0],features[y_kmeans == 1,1],s = 100, c = 'blue',label = 'cluster 2')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300, c = 'yellow',label='Centroids')
plt.title("clusters of drivers")
plt.xlabel('distance features')
plt.ylabel('speeding features')
plt.legend()

plt.show()


#fitting K-Means to the dataset with 4 clusters
kmeans = KMeans(n_clusters = 4,init = 'k-means++',random_state= 0)
y_kmeans = kmeans.fit_predict(features)

#Visulaing the clusters
plt.scatter(features[y_kmeans == 0,0],features[y_kmeans == 0,1],s = 100, c = 'red',label = 'cluster 1')
plt.scatter(features[y_kmeans == 1,0],features[y_kmeans == 1,1],s = 100, c = 'blue',label = 'cluster 1')
plt.scatter(features[y_kmeans == 2,0],features[y_kmeans == 2,1],s = 100, c = 'green',label = 'cluster 1')
plt.scatter(features[y_kmeans == 3,0],features[y_kmeans == 3,1],s = 100, c = 'cyan',label = 'cluster 1')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300, c = 'yellow',label='Centroids')
plt.title("clusters of drivers")
plt.xlabel('distance features')
plt.ylabel('speeding features')
plt.show()
