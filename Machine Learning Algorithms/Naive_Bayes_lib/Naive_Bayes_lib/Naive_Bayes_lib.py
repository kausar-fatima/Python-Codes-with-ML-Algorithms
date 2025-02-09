import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv(url, names=names)

# Separate features and labels
X = iris_data.iloc[:, :-1]  # Features
y = iris_data.iloc[:, -1]   # Labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the Naive Bayes classifier
naive_bayes_classifier = GaussianNB()
naive_bayes_classifier.fit(X_train, y_train)

# Example instance for prediction
test_instance = np.array([[4.9, 3.1, 1.5, 0.2]])

# Make a prediction
prediction = naive_bayes_classifier.predict(test_instance)
print(f'The predicted label for the instance {test_instance} is: {prediction[0]}')
