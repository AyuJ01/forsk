# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:33:28 2018

@author: tanmay
"""

import numpy as np 
import matplotlib.pyplot as plt
incomes=np.random.normal(100.0,20.0,10000)
plt.hist(incomes,50)
plt.show()
print(np.mean(incomes))
print(np.median(incomes))
incomes=np.append(incomes,[10000000000])
print(incomes)
print(np.mean(incomes))
print(np.median(incomes))