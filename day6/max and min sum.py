# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:16:18 2018

@author: Ayushi
"""

a = [1,2,3,4,5]
mini = min(a)
a.remove(mini)

sum1 = sum(a)
a.append(mini)
a.remove(max(a))

sum2 = sum(a)
print(sum2,sum1)