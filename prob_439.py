# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:56:23 2013

@author: olgis
"""


from time import time

def eu_sieve(num):     #sieve of Eratosthenes
    sieve = range(num+1)
    
    for x in xrange(2, int(len(sieve)**0.5) + 1):

        if sieve[x] != 0:
            for i in xrange(x+x, len(sieve), x):
                sieve[i] = 0
    
    sieve = [x for x in sieve[2:] if x != 0]
    
    return sieve
    
def gen_numbers(n):
    #NOT WORKING!!!
    s = []
    for i in (1, n):
        j = i + 1
        print i,j
        a = (i + j+1)**2
        s.append(a)
            
    return s
    
def calc_sum_of_primes(m):
    answer = 0
    
    primes = eu_sieve(m)
    print primes
    num_list = gen_numbers(m)
    print num_list
    
    for num in num_list:
        for l in xrange(len(primes)):
            if primes[l] <= num:
                if num % primes[l] == 0:
                    answer += primes[l]
                  
    return answer
        

start = time()
res = calc_sum_of_primes(3)
elapsed = time() - start

print res, elapsed