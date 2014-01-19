# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:48:04 2013

@author: olgis

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

PROBLEM: Find the sum of all the primes below two million.

"""
import time

def eu_sieve(num):     #sieve of Eratosthenes
    """ calculate list of primes up to num"""
    sieve = range(num+1)
    
    for n_prime in xrange(2, int(len(sieve)**0.5) + 1):

        if sieve[n_prime] != 0:
            for i in xrange(n_prime+n_prime, len(sieve), n_prime):
                sieve[i] = 0
    
    sieve = [n_prime for n_prime in sieve[2:] if n_prime != 0]
    
    return sieve
      
        
start = time.time()
product = sum(eu_sieve(int(2e6))) 
elapsed = time.time() - start

print "The sum of all the primes < 2 million is %s, found in %s sec" % (product, elapsed)
#The sum of all the primes below two million is 142913828922,
# found in 0.726412029266 sec
