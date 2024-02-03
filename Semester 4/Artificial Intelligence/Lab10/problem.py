# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:22 2020

@author: Alex
"""


class Problem:
    
    def __init__(self):
        self.texture={'very soft':[],
                      'soft':[],
                      'normal':[],
                      'resistant':[]
                      }
        
        self.capacity={'small':[],
                       'medium':[],
                       'high':[]
                       }
        
        self.cycle={'delicate':[],
                    'easy':[],
                    'normal':[],
                    'intense':[]
                    }      
        
        self.rules={'delicate':[],
                    'easy':[],
                    'normal':[],
                    'intense':[]
                    }     
        
        self.result={'delicate':[],
                    'easy':[],
                    'normal':[],
                    'intense':[]
                    }
        
        self.__readTexture()
        self.__readCapacity()
        self.__readCycle()
        self.__readRules()
        
    def __readTexture(self):
        with open('data\\texture.txt','r') as f:
            mylist=[]
            result=[]
            for line in f.readlines():
                mylist.append(line)
            result = []
            for line in mylist: 
                cpy = line.split(",")
                temp = []
                for no in cpy: 
                    temp.append(float(no))
                result.append(temp)
            
            for num in result[0]:
                self.texture['very soft'].append(num)
            
            for num in result[1]:
                self.texture['soft'].append(num)
            
            for num in result[2]:
                self.texture['normal'].append(num)
            
            for num in result[3]:
                self.texture['resistant'].append(num)
            
    def __readCapacity(self):
        with open('data\\capacity.txt','r') as f:
            mylist=[]
            result=[]
            for line in f.readlines():
                mylist.append(line)
            result = []
            for line in mylist: 
                cpy = line.split(",")
                temp = []
                for no in cpy: 
                    temp.append(float(no))
                result.append(temp)
            
            for num in result[0]:
                self.capacity['small'].append(num)
                
            for num in result[1]:
                self.capacity['medium'].append(num)
                
            for num in result[2]:
                self.capacity['high'].append(num)
    
    def __readCycle(self):
        with open('data\\cycle.txt','r') as f:
            mylist=[]
            result=[]
            for line in f.readlines():
                mylist.append(line)
            result = []
            for line in mylist: 
                cpy = line.split(",")
                temp = []
                for no in cpy: 
                    temp.append(float(no))
                result.append(temp)
            
            for num in result[0]:
                self.cycle['delicate'].append(num)
    
            for num in result[1]:
                self.cycle['easy'].append(num)
                
            for num in result[2]:
                self.cycle['normal'].append(num)
                
            for num in result[3]:
                self.cycle['intense'].append(num)
                
                
    def __readRules(self):
        with open('data\\rules.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                content = line.strip().split('-')
                self.rules[content[2]].append((content[0],content[1]))
    
