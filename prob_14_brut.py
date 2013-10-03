# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:32:11 2013

@author: olgis
"""
import time 

def nam(number):
    sequenceLength = 0
    startingNumber = 0
    sequence = 0
    
    for i in range(2,number+1):
        length = 1
        sequence = i
        while sequence != 1:
            
            if sequence % 2 == 0:
                sequence = sequence / 2
            else:
                sequence = sequence * 3 + 1
            
            length += 1
#Check if sequence is the best solution
        if length > sequenceLength:
             sequenceLength = length
             startingNumber = i
    return sequenceLength, startingNumber



start = time.time() 
product = nam(int(1e6))

elapsed = time.time() - start

print "The lenght of the longest sequence under 1 000 000 is %s by %s, found in %s sec." %(product[0], product[1], elapsed)
#The lenght of the longest sequence under 1 000 000 is (525, 837799), found in 31.2084360123 sec.