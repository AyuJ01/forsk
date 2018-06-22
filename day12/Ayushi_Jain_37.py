# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:06:45 2018

@author: Ayushi
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print(plt.hist(incomes,50))
print('mean',np.mean(incomes))
print('median',np.median(incomes))
incomes = np.append(incomes,10000000)
print(incomes)
print('mean',np.mean(incomes))
print('median',np.median(incomes))