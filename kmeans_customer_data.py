# -*- coding: utf-8 -*-
"""KMeans_Customer_Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nvD3aPXdCdMkbmeBrAbhO0WQbwm5Vn9O
"""

# import important library

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as np

# Load the dataset

df=pd.read_csv("/content/Customer-Data - 2.csv")

# Explore the dataset

df.head()

# Analyze the dataset

df.describe()

df.info()

df.isnull().sum()

df.columns

# Separate the feature and target variable

x=df.drop(['PURCHASES'],axis=1)
y=df['PURCHASES']

# Separate the feature and target variable

x=df.drop(['PURCHASES', 'CUST_ID'],axis=1) # Drop the 'CUST_ID' column
y=df['PURCHASES']

# split the dataset into training and testing sets.

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=45)

#  Normalize the features

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

# Apply K-Means clustring

kmeans=KMeans(n_clusters=5,random_state=45)
# Impute missing values using SimpleImputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean') # Replace missing values with the mean
x_train = imputer.fit_transform(x_train)
x_test = imputer.transform(x_test)


kmeans.fit(x_train)

# predict cluster on the test sets

y_pred=kmeans.predict(x_test)

from sklearn.metrics import silhouette_score
!pip install -q scikit-learn
silhouette_avg = silhouette_score(x_test, y_pred)
print("The average silhouette_score is :", silhouette_avg)

# visualize the cluster

import seaborn as sns
sns.scatterplot(x=x_test[:,0],y=x_test[:,1],hue=y_pred)

import matplotlib.pyplot as plt


plt.scatter(x_test[:,0],x_test[:,1],c=y_pred,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='black')
plt.show()

#filter rows of original data
filtered_label2 = x_train[kmeans.labels_ == 2] # Filter the training data x_train

filtered_label8 = x_train[kmeans.labels_ == 8] # Filter the training data x_train

#Plotting the results
plt.scatter(filtered_label2[:,0] , filtered_label2[:,1] , color = 'yellow')
plt.scatter(filtered_label8[:,0] , filtered_label8[:,1] , color = 'black')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Assuming kmeans and y_pred are defined from previous cells
u_labels = np.unique(kmeans.labels_)

#plotting the results:

for i in u_labels:
    plt.scatter(x_train[kmeans.labels_ == i , 0] , x_train[kmeans.labels_ == i , 1] , label = i) # Use x_train instead of df
plt.legend()
plt.show()



# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("/content/Customer-Data - 2.csv")

# Data Exploration
print(df.info())  # To get an idea of the data types and null values
print(df.describe())  # Summary statistics
print(df.isnull().sum())  # Checking for missing values

# Drop unnecessary columns and handle missing values
df = df.drop(columns=['CUST_ID'])  # Drop the customer ID column
df.fillna(df.mean(), inplace=True)  # Fill missing values with the mean

# Separate the features and the target (if applicable)
X = df.drop(columns=['PURCHASES'])
y = df['PURCHASES']

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Hyperparameter Tuning: Use Elbow Method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=45)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # Sum of squared distances of samples to their closest cluster center

# Plot the Elbow Method result
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Based on the Elbow plot, choose the optimal number of clusters (example: 3)
optimal_clusters = 3

# Apply K-Means with the chosen number of clusters
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=45)
y_pred = kmeans.fit_predict(X_scaled)

# Evaluate the model using silhouette score
silhouette_avg = silhouette_score(X_scaled, y_pred)
print("The average silhouette score is:", silhouette_avg)

# Visualize the clusters in 2D using PCA (Principal Component Analysis)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y_pred, palette="rainbow", legend='full')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering with 2D PCA')
plt.legend()
plt.show()

# Improved Visualizations for each cluster
unique_labels = np.unique(y_pred)
plt.figure(figsize=(8, 6))
for label in unique_labels:
    plt.scatter(X_pca[y_pred == label, 0], X_pca[y_pred == label, 1], label=f'Cluster {label}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black', marker='X', s=200, label='Centroids')
plt.title('Cluster Visualization after K-Means')
plt.legend()
plt.show()

