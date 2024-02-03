# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:55:57 2020

@author: Alex
"""

from random import shuffle


from chromosome import Chromosome
from population import Population
from utils import Utils
from numpy import random

class Controller:
    def __init__(self, trainingFilename, testingFileName, outputFilename):
        self.n = 0
        self.input = []
        self.output = []
        self.inputTesting = []
        self.outputTesting = []
        self.inputTraining = []
        self.outputTraining = []
        self.trainingFilename = trainingFilename
        self.testingFileName = testingFileName
        self.outputFilename = outputFilename

    def loadData(self):
        print("loading data...")
        with open(self.trainingFilename, "r") as f:
            Utils.HEADER = f.readline().split(',')[:-1]
            inputLines = f.readlines()
            shuffle(inputLines)
            for line in inputLines[:self.trainingSize]:
                values=list(line.strip("\n").split(","))
                mapvalues=list(map(float,values[:-1]))
                self.inputTraining.append(mapvalues[:])
                self.outputTraining.append(values[-1])
                self.n += 1
                
        
        with open(self.testingFileName, "r") as f:
            inputLines = f.readlines()
            shuffle(inputLines)
            for line in inputLines[:self.testingSize]:
                values=list(line.strip("\n").split(","))
                mapvalues=list(map(float,values[:-1]))
                self.inputTesting.append(mapvalues[:])
                self.outputTesting.append(values[-1])
                
        pair = list(zip(self.inputTesting, self.outputTesting))
        shuffle(pair)
        print("finished loading data")
        self.inputTesting, self.outputTesting = zip(*pair)
        
    def iteration(self, i):
        offspring = Population(self.nrOfIndividuals)
        for i in range(self.nrOfIndividuals):
            # select two parents for crossover
            first_pick=random.randint(0,self.nrOfIndividuals)
            second_pick=random.randint(0,self.nrOfIndividuals)
            while second_pick==first_pick:
                 second_pick=random.randint(0,self.nrOfIndividuals)
                 
            offspring.individuals[i] = Chromosome.crossover(self.population.individuals[first_pick],
                                                            self.population.individuals[second_pick],
                                                            self.crossoverProbability)
            
            offspring.individuals[i].mutate(self.mutationProbability)
            
        offspring.evaluate(self.inputTraining, self.outputTraining)
        
        self.population.join(offspring)
        self.population.selection(self.nrOfIndividuals)


        
    def run(self,nrOfIndividuals, iterations, trainingSize, testingSize, mutationProbability, crossoverProbability, epsilon):
        self.nrOfIndividuals = nrOfIndividuals
        self.trainingSize = trainingSize
        self.testingSize = testingSize
        self.iterations = iterations
        self.population = Population(self.nrOfIndividuals)
        self.mutationProbability = mutationProbability
        self.crossoverProbability = crossoverProbability
        self.epsilon = epsilon
        self.loadData()
        self.start()

        
    def start(self):
        currentAccuracy = 0
        while currentAccuracy < self.epsilon:
            
            self.population.evaluate(self.inputTraining, self.outputTraining)
    
            for index in range(self.iterations):
                print("Iteration: " + str(index+1))
                self.iteration(index)
                self.population.evaluate(self.inputTraining, self.outputTraining)
                
            best = self.population.best(1)[0]
            count = 0
            print("Training accurracy:", best.fitness,"%")
            
            for index in range(len(self.inputTesting)):
                if Utils.choose_category(best.predict(self.inputTesting[index])) == self.outputTesting[index]:
                    count += 1
                    
            currentAccuracy = float(count / len(self.inputTesting) * 100)
            print("Prediction accuracy:", currentAccuracy, "%\n\n")
            
        with open(self.outputFilename, "w") as f:
            f.write("Best expression: " + str(best.root))
            f.write("Correct guesses " + str(count))
            f.write("\nThat is " + str(currentAccuracy) + "%")
            


    