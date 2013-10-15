# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:25:47 2013

@author: olgis\

Starting with the number 1 and moving to the right in a clockwise direction
 a 5 by 5 spiral is formed as follows:

                        21 22 23 24 25
                        20  7  8  9 10
                        19  6  1  2 11
                        18  5  4  3 12
                        17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
PROBLEM:
    What is the sum of the numbers on the diagonals in a 1001 by 1001
    spiral formed in the same way?
"""

from time import time

def nxn(n_size):
    n = n_size//2
    a = 1
    for x in xrange(1, n+1):
        a = 4*(2*x + 1)**2 - 12*x + a
    
    return a
    
        
        
start = time()   
product = nxn(1001)
elapsed = time() - start

print "The sum of the diagonals in a 1001 x 1001 spiral is %s, found in %s sec." %(product, elapsed)
#The sum of the diagonals in a 1001 x 1001 spiral is 669171001, found in 0.000182867050171 sec.