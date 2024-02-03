# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:53:03 2020

@author: Alex
"""

from chromosome import Chromosome

class Population:
    def __init__(self, nrOfIndividuals):
        self.nrOfIndividuals = nrOfIndividuals
        self.individuals = [Chromosome() for i in range(nrOfIndividuals)]

    def evaluate(self, inputTraining, outputTraining):
        for chromosome in self.individuals:
            chromosome.computeFitness(inputTraining, outputTraining)

    def selection(self, n):
        #select the best n chromosomes 
        if n < self.nrOfIndividuals:
            self.nrOfIndividuals = n
            self.individuals = sorted(self.individuals, key=lambda x: x.fitness,reverse=True)
            self.individuals = self.individuals[:n]

    def best(self,m):
        # return the best m chromosomes
        self.individuals = sorted(self.individuals, key=lambda x: x.fitness,reverse=True)
        return self.individuals[:m]

    def join(self, children):
        # add the offsprings to the current individuals set
        self.nrOfIndividuals += children.nrOfIndividuals
        self.individuals = self.individuals + children.individuals