# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:38 2020

@author: Alex
"""

from algorithm import Algorithm 

class Controller:
    
    def __init__(self):
        self.algorithm = Algorithm()
        
    def jumpStep(self, start, stop, step):
        steps = []
        r = start
        while r <= stop:
            steps.append(r)
            r += step
        return steps 
    
    def run(self, texture, capacity): 
        """
        find the results
        """
        result=0
        for k in sorted(self.algorithm.problem.result.keys()):
            for i in range(len(self.algorithm.problem.rules[k])):
                """
                go through each rule and compute the result for the given texture/capacity w.r.t. to the input textures/capacities of the current rule
                """
                result =  min(self.algorithm.fuzzyTexture(texture,self.algorithm.problem.texture[self.algorithm.problem.rules[k][i][0]]),
                          self.algorithm.fuzzyCapacity(capacity,self.algorithm.problem.capacity[self.algorithm.problem.rules[k][i][1]]))
                
                if result!= 0 and result not in self.algorithm.problem.result[k]:
                    self.algorithm.problem.result[k].append(result)

           

        """
        points - list of points from the Cycle graphic,  of coordinates of type (x,y) where x=0, 0.2, ... , 0.8, 1 and y = result 
        maximum - the "best" result from the results dictionary, i.e. the cycle state which fits best given the current params
        """
        points=[]
        maximum = 0
        for k in sorted(self.algorithm.problem.result.keys()):
            
            if len(self.algorithm.problem.result[k]) != 0:
                maximum = max(self.algorithm.problem.result[k])
                
            """
            foreach point on the horizontal line 
            """
            for x in self.jumpStep(0.0,1.0,0.2):
                    """
                    fuzzify the point w.r.t. the cycles and take the maximum 
                    """
                    res = self.algorithm.fuzzyCycle(x, self.algorithm.problem.cycle[k])
                    if res > maximum:
                        res = maximum
                    if res != 0:
                        points.append((x,res))


        """
        indexes - a list of indexes, where for each index => points[index] needs to be removed
        an point (x,y) should be deleted from the list if there is another element "above" it, i.e. with the same x but larger y
        """
        indexes = []
        points = sorted(points)
        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                if points[i][0] == points[j][0] and points[i][1]>=points[j][1]:
                    indexes.append(j)
                    continue
                if points[i][0] == points[j][0] and points[i][1] <= points[j][1]:
                    indexes.append(i)

        """
        we delete the elements from list - points with the indexes from the "indexes" list
        """
    
        indexes.reverse()
        for i in indexes:
            del points[i]
  
        """
        compute the COA 
        """
        numerator = 0
        denominator = 0
        
        for (x,y) in points:
            numerator += x*y
            denominator += y
            
        res = numerator/denominator
        
        return res 
    
        