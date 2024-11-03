import numpy as np
from collections import Counter

# K-Nearest Neighbors (KNN) is one of the simpliest 
# supervised-learning algorithm in ML.

# KNN can be applied into both supervised-learning problems: 
# Classification and Regression

# In Classification, label of a new data point is directly inferred 
# from K nearest data points in training set

# In Regression, output of a data point is exactly equal to nearest given data
# point (K = 1), or is weighed average of output of nearest points

# Briefly, KNN is an algorithm which is searching for output of a data point
# by only using features of K nearest data points in the dataset,
# regardless of any noises in those points.

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))      # distance in Euclidean space (vector space)

class KNN:
    def __init__(self, k = 3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
        
    def _predict(self, x):
        # compute distances between new data point and existed ones.
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        
        # get K-nearest samples, labels
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        #majority, most common class
        most_common = Counter(k_nearest_labels).most_common(1)
        
        return most_common[0][0]
