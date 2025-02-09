import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

def kmeans(X, k, max_iterations=100):
    # Randomly initialize centroids
    centroids = X.values[np.random.choice(X.shape[0], k, replace=False)]
    
    for _ in range(max_iterations):
        # Assign each data point to the nearest centroid
        distances = np.linalg.norm(X.values[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Update centroids based on the mean of data points in each cluster
        for i in range(k):
            centroids[i] = np.mean(X.values[labels == i], axis=0)
            
    return labels, centroids

# Load data from CSV file
url = "data.csv.data"
column_names = ["sepalLength", "sepalWidth", "petalLength", "petalWidth", "plant"]
iris_data = pd.read_csv(url, header=None, names=column_names)

# Run K-means clustering
k = 3  # Number of clusters
labels_sepal, centroids_sepal = kmeans(iris_data[['sepalLength', 'sepalWidth']], k)  # Select sepal columns
labels_petal, centroids_petal = kmeans(iris_data[['petalLength', 'petalWidth']], k)  # Select petal columns

# Plot the data points and centroids in 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for Sepal features
scatter_sepal = ax.scatter(iris_data['sepalLength'], iris_data['sepalWidth'], labels_sepal, c=labels_sepal, cmap='viridis', marker='o', label='Sepal Data')
centroids_scatter_sepal = ax.scatter(centroids_sepal[:, 0], centroids_sepal[:, 1], np.arange(k), c='red', marker='X', s=200, label='Sepal Centroids')

# Scatter plot for Petal features
scatter_petal = ax.scatter(iris_data['petalLength'], iris_data['petalWidth'], labels_petal, c=labels_petal, cmap='viridis', marker='o', label='Petal Data')
centroids_scatter_petal = ax.scatter(centroids_petal[:, 0], centroids_petal[:, 1], np.arange(k), c='blue', marker='X', s=200, label='Petal Centroids')

ax.set_title('K-means Clustering on Iris Dataset (3D)')
ax.set_xlabel('Length (cm)')
ax.set_ylabel('Width (cm)')
ax.set_zlabel('Cluster')
ax.legend(loc='upper right')

plt.show()
