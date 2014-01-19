# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:34:37 2014

@author: olgis
"""
from __future__ import division
import re

dev_dict = []
num = 100

for x in range(2,num+1):
    print x
    res = 1/x
    print res
    match = re.search(r'(.+?)\1+', str(res))
    if match:
        print "Pattern is %s" %match.group(1)

