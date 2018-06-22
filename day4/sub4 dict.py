# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:56:55 2018

@author: Ayushi
"""

dict1={}
keys=['a','b','c']
dict1['a']=int(input("Enter element a : "))
dict1['b']=int(input("Enter element b : "))
dict1['c']=int(input("Enter element c : "))
print(dict1)
count=0


def fix_teen(dict1):
    count=0
    for num in dict1.values():    
        if num in range(13,20):
            if num==15 or num==16:
                count=count+num
            else:
                count=count+0
        else:
            count=count+num
    
    return count
print ("Sum = ",fix_teen(dict1))

"""
for num in dict1.values():
    fix_teen(num)
print(count)

"""


"""
for num in dict1.values():
    if num in range(13,20):
        if num==15 or num==16:
            count=count+num
        else:
            count=count+0
    else:
        count=count+num
print(count)

"""