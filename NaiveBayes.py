
import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        # X would be dataset
        # y would be classes
        
        n_samples, n_features = X.shape         # samples are rows, features are columns
        self._classes = np.unique(y)            # returning an array with number of unique classes        
        n_classes = len(self._classes)          
        
        # init mean, var, priors
        
        # 2-D array with class-row and feature-column
        self._mean = np.zeros((n_classes, n_features), dtype = np.float64) 
        self._var = np.zeros((n_classes, n_features), dtype = np.float64)
        
        self._priors = np.zeros(n_classes, dtype = np.float64) # 1-D array with size of n classes
        
        # estimate mean, var, P(c) for 
        for c in self._classes:
            X_c = X[c == y]
            self._mean[c, :] = X_c.mean(axis = 0)
            self._var[c, :] = X_c.var(axis = 0)
            self._priors[c] = X_c.shape[0] / float(n_samples)       # calculate the P(c)
            
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]      # return array of classes 
        return y_pred 
    
    def _predict(self, x):      # c = argmax{c in {1,.., C}}(P(c) * product{i = 1 -> d}(P(x_i | c)))
        
        # Naive conditional assumption that each data point is independent
        # The idea is that we will select class with the highest probability out of given C classes,
        # by using MAP (Maximum a Posteriori)
        
        posteriors = [] #init array of posteriors
        
        for idx in enumerate(self._classes):
            
            prior = np.log(self._priors[idx])                                # log(P(c))
             
            class_conditional = np.sum(np.log(self._prob_density_f(idx, x))) # log(sum{i = 1 -> d}(P(x_i | c)
            
            #calculate the probability of the data point in each class
            posterior = prior + class_conditional
            
            # append calculated posterior to array
            posteriors.append(posterior)
            
        return self._classes[np.argmax(posteriors)]         # return the class having the maximum probability
            
    #Gaussian Naive Bayes to calculate P(x_i | c)
    def _prob_density_f(self, class_idx, x):
        
        #mean, var are estimated using maximum likelihood
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        
        # Gaussian
        numerator = np.exp(-(x - mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator




