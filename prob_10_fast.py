# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:48:04 2013

@author: olgis

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

PROBLEM: Find the sum of all the primes below two million.

"""
import time

sieve = [True] * int(2e6) # Sieve is faster for 2M primes

def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]:
        mark(sieve, x)
      
        
start = time.time()
product = sum(i for i in xrange(2, len(sieve)) if sieve[i]) 
elapsed = time.time() - start

print "The sum of all the primes below two million is %s, found in %s sec" %(product, elapsed)
#The sum of all the primes below two million is 142913828922, found in 0.148223876953 sec