# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:03:15 2018

@author: tanmay
"""

import numpy as np
from scipy import stats
from collections import Counter 
x=np.random.randint(5,16,(40,))
print(x)
m=stats.mode(x)
print(m[0])

print(np.bincount(x).argmax())

print(Counter(x).most_common(1)[0][0])
d={}
for e in x:
    if e in d.keys():
        d[e]+=1
    else:
        d[e]=1
   
k=max(d.values())
l=d.keys()[d.values().index(k)]
print(l)