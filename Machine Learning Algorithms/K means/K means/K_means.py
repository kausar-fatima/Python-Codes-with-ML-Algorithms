import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the Iris dataset
url = "data.csv.data"
column_names = ["sepalLength", "sepalWidth", "petalLength", "petalWidth", "plant"]
iris_data = pd.read_csv(url, header=None, names=column_names)

# Drop the non-numeric column
numeric_data = iris_data.drop("plant", axis=1)

# Apply K-means clustering using scikit-learn for Sepal features
k_sepal = 3
kmeans_sepal = KMeans(n_clusters=k_sepal, random_state=42)
labels_sepal = kmeans_sepal.fit_predict(numeric_data.iloc[:, :2])  # Sepal features only
centroids_sepal = kmeans_sepal.cluster_centers_

# Apply K-means clustering using scikit-learn for Petal features
k_petal = 3
kmeans_petal = KMeans(n_clusters=k_petal, random_state=42)
labels_petal = kmeans_petal.fit_predict(numeric_data.iloc[:, 2:])  # Petal features only
centroids_petal = kmeans_petal.cluster_centers_

# Scatter plot for all features
plt.figure(figsize=(12, 8))

# Scatter plot for Sepal features
plt.subplot(2, 2, 1)
plt.scatter(numeric_data.iloc[:, 0], numeric_data.iloc[:, 1], c=labels_sepal, cmap='viridis', marker='o')
plt.scatter(centroids_sepal[:, 0], centroids_sepal[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-means Clustering of Sepal Features")
plt.xlabel("sepalLength")
plt.ylabel("sepalWidth")
plt.legend()

# Scatter plot for Petal features
plt.subplot(2, 2, 2)
plt.scatter(numeric_data.iloc[:, 2], numeric_data.iloc[:, 3], c=labels_petal, cmap='viridis', marker='o')
plt.scatter(centroids_petal[:, 0], centroids_petal[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-means Clustering of Petal Features")
plt.xlabel("petalLength")
plt.ylabel("petalWidth")
plt.legend()

# Scatter plot for Sepal and Petal features
plt.subplot(2, 2, 3)
plt.scatter(numeric_data.iloc[:, 0], numeric_data.iloc[:, 1], c=labels_sepal, cmap='viridis', marker='o', label='Sepal Clusters')
plt.scatter(centroids_sepal[:, 0], centroids_sepal[:, 1], c='red', marker='X', s=200, label='Sepal Centroids')
plt.scatter(numeric_data.iloc[:, 2], numeric_data.iloc[:, 3], c=labels_petal, cmap='plasma', marker='s', label='Petal Clusters')
plt.scatter(centroids_petal[:, 0], centroids_petal[:, 1], c='blue', marker='X', s=200, label='Petal Centroids')
plt.title("K-means Clustering of Sepal and Petal Features")
plt.xlabel("Sepal Length / Petal Length")
plt.ylabel("Sepal Width / Petal Width")
plt.legend()

plt.tight_layout()
plt.show()
