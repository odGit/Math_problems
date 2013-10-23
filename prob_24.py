# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:36:20 2013

@author: olgis

A permutation is an ordered arrangement of objects.The lexicographic
 permutations of 0, 1 and 2 are:

                012   021   102   120   201   210

PROBLEM: 
    What is the millionth lexicographic permutation of the digits 0 - 9?

SOLUTION: To find the 1e6th combination of 10 digits, we need to calculate possible permutations of digits from 0 to 9.
10 digits can be placed in 10! = 3 528 800 ways
9  digits can be placed in 9!  =   352 880 ways
8  digits can be placed in 8!  =    40 320 ways
From where we can see that between 
01 23 45 67 89
10 23 45 67 89 
is 9! numbers. Based on this we can say that 1e6 is in block 1e6 // 9! is 2. We can repeat for the reminding untill remindning is not 0 (Q = R//B, where R is reminder searched and B is block size)
For example R = 1e6:
    Q1 = 1e6 // 352 880 = 2
    [0, 1, (2), 3, 4, 5, 6, 7, 8, 9]
    Q2 = 274 240 // 40 320 = 6
    [0, 1, 3, 4, 5, 6, (7), 8, 9]
    ...
    
The number which we will find is 1 000 001st so the number before is the one we are looking. 
"""

from time import time
from math import factorial

def looking_for_solution(n,r):
    digits = [x for x in range(n+1)]
    b = [factorial(u) for u in range(n,0, -1) if factorial(u) <= r]
    answer = ''
    for j in b:
        q = r//j
        r -= q*j  #update reminder
        if q == 0:
            for g in digits:
                answer += str(g)
        else:
            answer += str(digits.pop(q))
    return answer
    
start = time()
result = looking_for_solution(9,int(1e6))
elapsed = time() - start

print "The million 1st number is %s, found in %s sec." %(result, elapsed)
#found in 0.000101089477539 sec