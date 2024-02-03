# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:27:17 2020

@author: Alex
"""

import numpy as np
from statistics import mean

"""
Linear Regression with the Least Squares method. 
Fitting (i.e. determining the coefficients) is done using the formula: 
    B = (X' * X)^-1 * X' * Y
    where B = the unknown coefficients
    X = [[x11....x15]
         [x21....x25]
         ...........
         [xn1....xn5]] 
    Y = [y1....yn]
"""

class LinearRegression: 
    
    def __init__(self):
        self.betas = None
    
    def error(self, y_predicted, y):
        """
        Use the least squares method to define error[i]=(y_from_dataset[i] - y_predicted[i]) ^ 2
        Draw a conclusion for all dataset by computing the mean of all errors.
        """
        errors = []
        for i in range(y.size): 
            errors.append((y[i]-y_predicted[i]) ** 2)
        return mean(errors)
    
    def fit(self, x, y):
        """
        Compute the beta coefficients with the formula from above. 
        """
        extra_ones = np.array([1.0 for i in range(len(x))],dtype='f').reshape(-1,1) # create an extra column of ones (neutral elements)
         
        x = np.concatenate((extra_ones,x),1) # append extra ones to x with axis 1 because we want a matrix 
        xt = x.transpose()
        
        # multiply matrices
        self.betas = np.linalg.inv(xt.dot(x)).dot(xt).dot(y)
            
        
    def sumForRow(self, row):
        """
        Compute f(x), i.e. b0 + sum(xi*bi), i=1,n, x=row
        """
        s = float(self.betas[0]) # b0 has no match in x
        for i in range(row.size):
            s+=(row[i]*self.betas[i+1])
        return s