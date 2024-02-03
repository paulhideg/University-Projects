# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:42 2020

@author: Alex
"""

from controller import Controller 

class UI:
   
    def __readInput(self):
        with open ('input.in','r') as f: 
            try: 
                tex = float(f.readline())
                cap = float(f.readline())
                return (tex,cap)
            except TypeError:
                return None
            except ValueError:
                return None
        
    def __findCycle(self, texture, capacity): 
        c = Controller()
        
        print("Textures input:")
        print(c.algorithm.problem.texture)
        print("-"*60)
        print("Capacities input:")
        print(c.algorithm.problem.capacity)
        print("-"*60)
        print("Cycles input:")
        print(c.algorithm.problem.cycle)
        print("-"*60)
    
        print("Texture:{}".format(texture))
        print("Capacity:{}".format(capacity))
        
        result = c.run(texture,capacity)
        print("Result cycle:{}".format(round(result,2)))
        
        with open('output.out', 'w') as f:
            f.write(str(round(result,2)))
            
    def run(self): 
        while True: 
            print("run/exit")
            print(">>")
            cmd = input()
            if cmd=="exit":
                return 
            else:
                (texture, capacity) = self.__readInput()
                if (texture, capacity) is None: 
                    continue
                else: 
                    self.__findCycle(texture, capacity)
        