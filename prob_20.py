# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:35:54 2013

@author: olgis

Problem: Find the  factorial of 100

"""

import time

def factor(n):
    res = 1
    for n in range(1,n+1):
        res *= n
    return res

def frac_dig_sum(num):
    prod = 0
    for dig in str(num):
        prod += int(dig)
    return prod


start = time.time()
product = frac_dig_sum(factor(100))
elapsed = time.time() - start

print "Factorial is %s, found in %s sec" % (product, elapsed)
