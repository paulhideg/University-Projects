# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:27:33 2020

@author: Alex
"""
from regression import LinearRegression
import numpy as np
from matplotlib import pyplot as plt 

class Controller: 
    
    def __init__(self, filename):
        self.__filename = filename
        
    def __readData(self):  
        data = []
        
        with open(self.__filename, 'r') as f: 
            lines = f.readlines()
            for line in lines:
                split = line.split(' ')
                if len(split)==1: #skip empty lines
                    continue
                data.append([float(num) for num in split])
        
        x=[]
        y=[]
        for line in data: 
            x.append(line[:-1])
            y.append(line[-1])
        return np.array(x,dtype='f'),np.array(y,dtype='f')
    
    
    def run(self): 
        x,y = self.__readData()
        model = LinearRegression()
        model.fit(x,y)
        y_predicted = [model.sumForRow(row) for row in x]
        
        # this plot is just to make sure we get values of a linear function
        plt.scatter(y,y_predicted,c='r')
        plt.show()
        
        mean_error = model.error(y_predicted,y)
        return mean_error
    