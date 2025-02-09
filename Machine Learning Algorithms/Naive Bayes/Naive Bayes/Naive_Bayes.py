import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
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

# Helper function to calculate probabilities
def calculate_probabilities(data, label_column):
    probabilities = {}
    labels, counts = np.unique(data[:,label_column], return_counts=True)  # extracts unique labels (labels) and 
                                                                          # their corresponding counts (counts) from the specified column.
    total_samples = len(data)  # total number of samples in the dataset.
    for label, count in zip(labels, counts):  # iterates through each unique label
        probabilities[label] = count/total_samples
    return probabilities
    
# Helper function to train Naive Bayes classifier
def train_naive_bayes(X, y):
    num_features = X.shape[1]  # returning the second element of the tuple, which is the number of 
                               # columns or features in the feature matrix X.
    unique_labels = np.unique(y)  # extracts the unique labels from the target variable y
    probabilities = {}
    
    for label in unique_labels:  # iterates over each unique label in the dataset
        label_indices = np.where(y == label)[0]  # assigns to label_indices the array of indices where 
                                                 # the label is equal to the current label
        label_data = X.iloc[label_indices]  # extracts the rows from the feature matrix X that 
                                            # correspond to instances of the current class
        
        probabilities[label] = []  # list for the current label in the probabilities dictionary.
        for i in range(num_features):  #  iterates over each feature in the dataset.
            feature_values, counts = np.unique(label_data.iloc[:, i], return_counts=True)  #  unique values and their counts in the 
                                                                                           #  instances belonging to the current class.
            feature_probabilities = dict(zip(feature_values, counts/len(label_data)))  #  unique values of the feature are keys, 
                                                                                       # and their corresponding probabilities are values.
            probabilities[label].append(feature_probabilities)
    return probabilities

# function to predict_naive_bayes classifier
def predict_naive_bayes(instance, probabilities):
    predicted_label = None   # store the label with the maximum probability.
    max_probability = -1   #  to keep track of the maximum probability encountered during the loop
    for label,label_probabilities in probabilities.items():  # this loop iterates over each key-value pair in the probabilities dictionary.
        instance_probability = 1.0
        for i, value in enumerate(instance):  # iterates over each feature value in the given instance.
            if value in label_probabilities[i]:  # label_probabilities[i] is the dictionary containing the 
                                                 # probabilities of each unique feature value for the current label and feature.
                instance_probability *= label_probabilities[i][value]
            else:
                instance_probability = 0 # if value is unseen in training data, probability is 0
                
        if instance_probability > max_probability:
            max_probability = instance_probability
            predicted_label = label
    return predicted_label

# Train the Naive Bayes classifier
probabilities = train_naive_bayes(X, y)

# Example instance for prediction
test_instance = [4.9, 3.1, 1.5, 0.2]

# Make a prediction
prediction = predict_naive_bayes(test_instance, probabilities)
print(f'The predicted label for the instance{test_instance} is: {prediction}')