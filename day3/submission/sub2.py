# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:33:25 2018

@author: Ayushi
"""
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
b=numbers.index(237)
#print(b)
subnumber=numbers[:b]
print(subnumber)
for i in subnumber:
    if(i%2==0):
        print(i)