# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:22:18 2013

@author: olgis



The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

SOLUTION: Reverse Collatz Graph http://en.wikipedia.org/wiki/Collatz_conjecture

        {2n}             if n = 0,1
R(n) =                                      (mod 3)
        {2n, (2n-1)/3}    if n = 2

"""
import time

def collatz(n):
    if n % 2 == 0:
        return n/2
        
    return 3*n + 1
    
def find_sequence(n):
    dict_seq = {}
    
    for k in range(n,2,-1):
        current_seq = []
        current_seq. append(k)
        
        while current_seq[-1] not in dict_seq:

            if current_seq[-1] != 1:
                k = collatz(k)
                current_seq.append(k)

            else:
                for i in current_seq:
                    dict_seq[i] = len(current_seq) - current_seq.index(i)
#                    print dict_seq

        if current_seq[-1] in dict_seq:
            for i in current_seq:
                m = len(current_seq) - current_seq.index(i)
                n = dict_seq[current_seq[-1]]
                dict_seq[i] = m + n


    return max(dict_seq, key=dict_seq.get), max(dict_seq.values(), key=int)
        
start = time.time() 
product = find_sequence(int(1e6))
elapsed = time.time() - start

print "The lenght of the longest sequence under 1 000 000 is %s with %s, found in %s sec." %(product[0], product[1], elapsed)
#The lenght of the longest sequence under 1 000 000 is 837799 with 537, found in 7.35239601135 sec.