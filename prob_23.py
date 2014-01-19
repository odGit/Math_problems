# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:50:47 2013

@author: olgis

Deficient number - the sum of its proper divisors is less then number itself 
Abundant number - the sum of its proper divisors is GREATER then number itself.

By mathematical analysis can be shown that all integers > 28123 can be written
as the sum of two abundant numbers.

Find the sum of all the positive integers which can NOT be written as the sum
 of two ABUNDANT numbers.

Solution:
    Number range: all numbers from 0 to  28 123
    1. remove all prime numbers 
    
"""

import time
import math

def eu_sieve(seed):     #sieve of Eratosthenes
    primes = seed[:]
    
    for x in xrange(2, int(len(primes)**0.5) + 1):
        if primes[x] != 0:
            for i in xrange(x+x, len(primes), x):
                primes[i] = 0
    
    not_primes = [x for x in seed if x not in primes] #list, excluding PRIMES
    
    return not_primes
    
    
    
def find_all_divisors(number):
    divList = [1] #initiatin a list with 1, all numbers can be divided by 1
    y = 2
    a = math.sqrt(number)
    
    while y <= a:
        if number % y == 0:
            divList.append(y)
            dev_res = number/y
            if dev_res not in divList and dev_res != number:
                divList.append(dev_res)
            
        y += 1
        
    return divList
    
    
    
def keep_only_abundant(num_list):
    a = num_list[:]
    other = []
    for n in a:
        if sum(find_all_divisors(n)) <= n :
            other.append(n)
    
    result = [x for x in a if x not in other]
    
    return result
    
    
            
def search_not_abund_sum(all_num, only_abund):
    
    while len(only_abund) > 1:
        first_in_list = only_abund.pop(0)

        lim_num = all_num[-1] - first_in_list
        new_list = [k for k in only_abund if k <= lim_num]
        
        for number in new_list:
            abund_sum = first_in_list + number
            
            if abund_sum in all_num:
                all_num.remove(abund_sum)
                
    return all_num
        

start = time.time()

init_list = range(28123 + 1)

num_excl_primes = eu_sieve(init_list)

only_abund_list = keep_only_abundant(num_excl_primes)


res = search_not_abund_sum(init_list, only_abund_list)

elapsed = time.time() - start
print "The sum is %s, it took %s sec." %(sum(res), elapsed)

"""
You're testing every number between 1 and the limit (let's say 30000)
 against every abundant number, so you're doing roughly 30000 * 7428
 iterations; and you're checking if the result is in a list, which is
 a very slow operation -- it checks every item on the list until it
 finds a match!

Instead, you should generate every number that is a sum of two abundant
 numbers. At the most, that would take 7428 * 7428 iterations -- fewer
 if properly executed (hint: avoid checking both a + b and b + a by
 ensuring that b is always >= a; and as someone else suggested, be sure
 to stop when sums get too large). Mark those numbers off a list of numbers
 below limit and sum the remaining numbers.
"""