# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:36:14 2013

@author: olga Dmitricenko

Brute Force solution.

Problem: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

To don't loop for A & B  from 1 to SUM. Will use the facts that A < B < C,
from where follows that A < SUM/3, and B < SUM/2
"""

import time

def triplet_with_sum(m):
    for a in range(1, m//3):  #A < SUM/3
        for b in range(1, m//2): # B < SUM/2
            c = m - a - b
            if a*a + b*b == c*c:
                print "The Pythagorean triple is %d, %d, %d"  % (a, b, c)
                return a*b*c
                
    return 0
    
start = time.time()
product = triplet_with_sum(1000)
elapsed = (time.time() - start)


print "abc = %s, found in %s sec" % (product, elapsed)



#The Pythagorean triple is 200, 375, 425
#abc = 31875000, found in 0.0332520008087 sec        