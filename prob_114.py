# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:22:25 2013

@author: olgis

Problem:
    How many ways can a row measuring fifty units in length be filled?
"""

from time import time

memo = dict()

def filling(size, units): 
    if units < size: return 1
    if units == size: return 2
    if memo.has_key((size, units)): return memo[(size, units)]
    ways = 1
    for s in xrange(size, units + 1):
        for p in xrange(0, units-s + 1):
            ways += filling(size, units - (s+p+1))
    memo[(size,units)] = ways
    return ways
 

            
start = time()   
product = filling(3, 50) #max block size, units
elapsed = time() - start

print "Can be filled in %s ways, found in %s sec." %(product, elapsed)

#found in 0.0170528888702 sec.