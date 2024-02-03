# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:52:16 2020

@author: Alex
"""

import numpy as np
from random import randint, choice
from math import sin, cos
from utils import Utils
from node import Node

DEPTH_MAX = 7

class Chromosome:
    def __init__(self, d=DEPTH_MAX):
        self.fitness = 0
        self.root = Node()
        self.root.create(d)

    """
    What the exec basically does is to "bind" the string "valueX" to the actual numeric value.
    This needs to happen because when eval(exp) is called, an operation like value1*value2 has to be done with their associated integer values, 
    and not with strings.
    """
    def computeFitness(self, inputTraining, outputTraining):  
        self.fitness = 0
        exp = str(self.root)
        count=0
        
        for (x, y) in zip(inputTraining, outputTraining):
            for index in range(len(x)):
                exec("{} = {}".format(Utils.HEADER[index], x[index]))
                
            res = eval(exp)
            if Utils.choose_category(res) == y:
                count += 1
                
        self.fitness = float(count / len(inputTraining) * 100)
        
        return self.fitness
    
    def predict(self, inputData):
        exp = str(self.root)
        for i in range(len(inputData)):
            exec("{} = {}".format(Utils.HEADER[i], inputData[i]))
        return eval(exp)


    def crossover(parent1, parent2, crossoverProbability):
        if np.random.uniform(0,1)>crossoverProbability:
            # pick two random nodes i.e. expressions from each parent
            node1 = choice(parent1.root.getNodes())
            node2 = choice(parent2.root.getNodes())
            child = Chromosome()
            if parent1.root == node1:  # if we must change the whole tree
                child.root = node2.deepcopy()
            else:
                child.root = Node()
                child.root.change(parent1.root, node1, node2)
            return child
        return parent1

    def mutate(self, mutationProbability):
        if np.random.uniform(0,1)>mutationProbability:
            pos = randint(1, self.root.size)
            self.root.mutate(pos,DEPTH_MAX)
