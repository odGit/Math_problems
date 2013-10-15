# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:26:15 2013

@author: olgis

Ecercise: 
    Given that L is the length of the wire, for how many values of 
    L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

SOLUTION:
    This problem can be solved using the same technique as described in
    problem 9.
"""

from fractions import gcd
from time import time

def one_way_triplet(limit):
    mlimit = int(limit ** 0.5)
    count = 0
    sieve = [0] * (limit + 1)
    
    for m in xrange(2, mlimit + 1):
        for n in range(2 if m % 2 else 1, m + 1, 2):
            if gcd(m, n) == 1:
                a = m*m - n*n
                b = 2 * m * n
                c = m*m + n*n
                res = a + b + c
                if res > limit: break
                for j in range(res, limit, res): sieve[j] += 1
                
    for i in sieve:
        if i == 1: count += 1
            
    return count
    
    
start = time()
product =  one_way_triplet(int(1.5e6))
elapsed = time() - start


print "There are %s triangles which can be bent one way. Found in %s s" % (product, elapsed)
#There are 161667 triangles which can be bent one way. Found in 0.581925868988 s