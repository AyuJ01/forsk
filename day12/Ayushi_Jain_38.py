# -*- coding: utf-8 -*-
"""
Created on Mon May 28 22:48:56 2018

@author: Ayushi
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150, 20, 1000)
print(plt.hist(incomes,100))
print('std ',np.std(incomes))
print('var ',np.var(incomes))
