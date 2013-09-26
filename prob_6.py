# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:35:54 2013

@author: olgis

Problem: Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

"""

import time

def evenly_devisible(k_max):
    sum_sqr = sum = 0
    for kx in range(1, k_max+1):
        sum_sqr = sum_sqr + kx**2
        sum = sum + kx 
    return sum**2 - sum_sqr

start = time.time()
product = evenly_devisible(100)
elapsed = time.time() - start

print "The difference is %s, found in %s sec" % (product, elapsed)