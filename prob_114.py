# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:22:25 2013

@author: olgis

Problem:
    How many ways can a row measuring fifty units in length be filled?
"""

from time import time

memo = dict()
def filling(size, tiles): 
    if tiles<size: return 1
    if tiles==size: return 2
    if memo.has_key((size,tiles)): return memo[(size,tiles)]
    ways = 1
    for s in xrange(size, tiles + 1):
        for p in xrange(0, tiles-s + 1):
            ways += filling(size, tiles - (s+p+1))
    memo[(size,tiles)] = ways
    return ways
 

            
start = time()   
product = filling(3,50) #1st size, tiles
elapsed = time() - start

print "Can be filled in %s ways, found in %s sec." %(product, elapsed)

#16475640049