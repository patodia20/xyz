# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 00:28:48 2018

@author: Anwesha
"""

import copy
class Waterjug:


    def __init__(self,am,bm,a,b,g):
        self.a_max = am
        self.b_max = bm
        self.a = a
        self.b = b
        self.goal = g


    def fillA(self):
        self.a = self.a_max
        #print ('(', self.a, ',',self.b, ')')


    def fillB(self):
        self.b = self.b_max
        #print ('(', self.a, ',', self.b, ')')


    def emptyA(self):
        self.a = 0
        print ('(', self.a, ',', self.b, ')')


    def emptyB(self):
        self.b = 0
        #print ('(', self.a, ',', self.b, ')')

    # TODO Correct Algo..
    def transferAtoB(self):
        while (True):
            self.a = self.a - 1            
            self.b = self.b + 1
            if (self.a == 0 or self.b == self.b_max):
                break
        #print ('(', self.a, ',', self.b, ')')

    # TODO Correct Algo..
    def transferBtoA(self):
        while (True):
            self.b = self.b - 1            
            self.a = self.a + 1
            if (self.b == 0 or self.a == self.a_max):
                break
        #print ('(', self.a, ',', self.b, ')')

    def graph(self):
       
        while (True):
            if (self.a, self.b) in states:
               states.append((self.a, self.b))
               states.pop(-1)
            pass
            if (self.a == self.goal or self.b == self.goal):
                states.append((self.a, self.b))
                result=copy.deepcopy(states)
                res.append(result)
                #print ('(', self.a, ',', self.b, ')')
                break 
            if (self.a == 0):
                states.append((self.a, self.b))
                self.fillA()
            elif (self.a > 0 and self.b != self.b_max):
                states.append((self.a, self.b))
                self.transferAtoB()
            elif (self.a > 0 and self.b == self.b_max):
                states.append((self.a, self.b))
                self.emptyB()
            else:
                if (self.b == 0):
                    states.append((self.a, self.b))
                    self.fillB()
                    
                elif (self.b > 0 and self.a != self.a_max):
                      states.append((self.a, self.b))
                      self.transferBtoA()
                      
                elif (self.b > 0 and self.a != self.a_max):
                      states.append((self.a, self.b))
                      self.emptyA()

if __name__ == "__main__":
    states=list()
    result=[]
    res= []
    waterjug=Waterjug(4,3,0,0,2)
    waterjug.graph()
    for var in  range(len(res)) :
        print("{}Liters".format(res[var]))
        
        
        
        ## edit some changes 
