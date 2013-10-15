# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:22:25 2013

@author: olgis

Problem:
    How many ways can a row measuring fifty units in length be filled?
"""

from time import time

def filling(units,n):
    solution = 2 #counting the case when all empty +1 and units == n
    for position in xrange(0, (units-n)+1):
        for block_length in range(n, (units-position) + 1):
            solution +=1
#            print position
#            print block_length
    return solution
            
start = time()   
product = filling(50,3) #1st UNITS, 2nd 
elapsed = time() - start

print "in %s ways, found in %s sec." %(product, elapsed)

#16475640049