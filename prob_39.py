# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:26:15 2013

@author: olgis

If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.
 {20,48,52}, {24,45,51}, {30,40,50}

Ecercise: 
    For which value of p ≤ 1000, is the number of solutions maximised?


SOLUTION:
    This problem can be solved using the same technique as described in
    problem 9.
"""

from fractions import gcd
from time import time

def one_way_triplet(limit):
    mlimit = int(limit ** 0.5)
    sieve = [0] * (limit + 1)
    
    for m in xrange(2, mlimit + 1):
        for n in range(2 if m % 2 else 1, m + 1, 2):
            if gcd(m, n) == 1:
                a = m*m - n*n
                b = 2 * m * n
                c = m*m + n*n
                res = a + b + c
                if res > limit: break
                for j in range(res, limit, res): 
                    sieve[j] += 1
     
    a = max(sieve)
    b = sieve.index(a)
    return b, a
    
    
start = time()
product =  one_way_triplet(int(1e3))
elapsed = time() - start


print "For the value of p = %s, with max %s. Found in %s s" % (product[0], product[1], elapsed)
#For the value of p = 840, with max 8. Found in 0.000361204147339 s