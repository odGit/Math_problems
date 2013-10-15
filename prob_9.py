# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:26:15 2013

@author: olgis

Ecercise: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

THEORY
Euclid solution for Pythagorean Triplets can be generated following:
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
where int m and int n is  m > n > 0.

Important: 
    1) Depending on the choices of m and n,might be necessary to interchange
a and b to adhere to the constraint a < b.
    2) From every Pythagorean triplet can be generated a primitive triplet 
by dividing by the greatest common divisor (of a,b,c):
    a = d*(m**2 - n**2)
    b = d*2*m*n
    c = d*(m**2 + n**2)
 ! with m > n > 0,
 !! m and n being coprimes and ONLY one is even.
 
SOLUTION 
 s = a + b + c = d*(m**2-n**2) + 2d*m*n + d*(m**2+n**2) = 2m*(m+n)*d, follows
  m     is a divisor for s//2
  m + 2 is a dicisor for s//(2*m)
  m < k < 2*m
  k < s//(2*m)
  k is ODD and gcd(m,k) == 1
"""

import math
from fractions import gcd
import time

def triplet_with_sum(s):
    mlimit =int( math.sqrt(s//2))
    for m in range(2, mlimit+1):
        if (s//2) % m == 0:    #found m
            if m % 2 == 0:
                k = m + 1 # m is odd --> k is even
            else:
                k = m + 2 
        while k < (2*m) and k <= (s/(2*m)) :
            if (s / (2*m)) % k == 0 and gcd(k,m) == 1:
                d = s/2/(k*m)
                n = k - m
                a = d*(m**2 - n**2)
                b = d*2*m*n
                c = d*(m**2 + n**2)
                print "The Pythagorean triple is %d, %d, %d"  % (a, b, c)
                return a+b+c
            k += 2
    return 0
    
    
start = time.time()
product = triplet_with_sum(1000)
elapsed = time.time() - start


print "abc = %s, found in %s sec" % (product, elapsed)

#The Pythagorean triple is 375, 200, 425
#abc = 31875000, found in 5.91278076172e-05 sec