# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:54:37 2018

@author: tanmay
"""

import numpy as np
import matplotlib.pyplot as plt
incomes=np.random.normal(150,20,1000)
plt.hist(incomes,100)
plt.show()
print(np.std(incomes))
print(np.var(incomes))