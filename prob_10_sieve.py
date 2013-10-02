# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:48:04 2013

@author: olgis

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

PROBLEM: Find the sum of all the primes below two million.

"""
import time

def eu_sieve(num):     #sieve of Eratosthenes
    sieve = range(num+1)
    
    for x in xrange(2, int(len(sieve)**0.5) + 1):

        if sieve[x] != 0:
            for i in xrange(x+x, len(sieve), x):
                sieve[i] = 0
    
    sieve = [x for x in sieve[2:] if x != 0]
    
    return sieve
      
        
start = time.time()
prime_list = eu_sieve(int(2e6))
product = sum(prime_list) 
elapsed = time.time() - start

print "The sum of all the primes below two million is %s, found in %s sec" %(product, elapsed)
#The sum of all the primes below two million is 142913828922, found in 0.726412029266 sec
