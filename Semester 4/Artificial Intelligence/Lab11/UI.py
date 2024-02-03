# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:09:04 2020

@author: Alex
"""

from controller import Controller

"""
Dataset has been split 70/30 for training/testing.
"""
class Console:
    def __init__(self):
        self.__controller = Controller("data\\training.in", "data\\testing.in", "results.log")
        
    def __readParams(self): 
        with open('data\\params.in', 'r') as f:
            nrIndividuals = int(f.readline())
            iterations = int(f.readline())
            trainingSize = int(f.readline())
            testingSize = int(f.readline())
            mutationProbability = float(f.readline())
            crossoverProbability = float(f.readline())
            epsilon = float(f.readline())
            return nrIndividuals, iterations, trainingSize, testingSize, mutationProbability, crossoverProbability, epsilon
        
    def run(self):
        while True:
            print("run/exit")
            print(">>")
            cmd = input()
            if cmd == 'run':
                nrOfIndividuals, iterations, trainingSize, testingSize, mutationProbability, crossoverProbability, epsilon = self.__readParams()
                self.__controller.run(nrOfIndividuals, iterations, trainingSize, testingSize, mutationProbability, crossoverProbability, epsilon)
            else:
                return

