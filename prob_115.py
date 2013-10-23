# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:22:25 2013

@author: olgis

Problem:
  For m = 50, find the least value of n for which the fill-count function first exceeds one million.
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

def less_then(num, n):
    for m in xrange(n*2, n*4):
        b = filling(n,m)
        if b > num:
            return m
    return 0
            
start = time()   
product = less_then(int(1e6), 50) #max, block size(n)
elapsed = time() - start

print "Can be filled in %s ways, found in %s sec." %(product, elapsed)

#found in 0.117833852768 sec