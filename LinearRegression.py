import numpy as np

class LinearRegression:
    def __init__(self, lr = 0.001, n_iters = 1000):
        self.lr = lr                                                    # lr is learning rate
        self.n_iters = n_iters                                          
        self.weights = None                                             # in original formula, w is theta_1, 
        self.bias = None                                                # b is theta_2
        
    # To achive the best-fit of regression line, 
    # this model aims to predict the target value y such that 
    # the error difference between the y_predicted value 
    # and y (true) value is minimum.
        
    def fit(self, X, y):
        #init param
        n_samples, n_features = X.shape
        
        # one we find the weights and bias, we get a best-fit line
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Deploying Mean Square Error (MSE) cost function, 
        # which calculates the average of squared error
        # between y_pred and y (true value).
        
        # The loop will continuously adjust the w, b parameter.
        # This ensure that the MSE value converges to the global minima,
        # signifying the most accurate fit of the linear regression line of the dataset
        
        for _ in range(self.n_iters):
            # updating y_pred value for the next iteration
            y_predicted = np.dot(X, self.weights) + self.bias           # y^ = x * w (coefficent of x) + b (intercept), 
                                                                        # using dot product since x is a vector

            # Mean Square Error negative gradient, which is
            # updating the weights and bias parameter.

            # derivative of cost function J with respect of y_predicted.
            dw = (1/n_samples) * (np.dot(X.T, (y_predicted - y)) * 2)
            
            # derivative of cost function J with respect of y.
            db = (1/n_samples) * np.sum((y_predicted - y) * 2)
            
            # adjusting the w, b parameter
            self.weights -= self.lr * dw                                # w = w - lr * dw
            self.bias -= self.lr * db                                   # b = b - lr * db
     
    # final step with optimized weights and bias parameters
    def predict(self, X):
        y_predicted = np.dot(X, self.weights) * self.bias
        return y_predicted
    

    



