# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:35:54 2013

@author: olgis

Problem: Latice path. How many such routes are there through a 20×20 grid?
"""

import time
 
def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)

print "%s found in %s seconds" % (n,elapsed)