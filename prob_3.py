# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:35:54 2013

@author: olgis

Problem: What is the largest prime factor of the number 600851475143 ?

"""

import time

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def high_prime(n):
    x = 3
    k = 0
    while x < int(n**0.5)+1:
        if isprime(x):
            if n % x == 0:
                k = x
        x = x + 2
    return k
    
start = time.time()
product = high_prime(600851475143)
elapsed = time.time() - start

print "The sum is %s, found in %s sec" % (product, elapsed)