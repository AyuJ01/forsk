# -*- coding: utf-8 -*-
"""
Created on Mon May 14 00:23:21 2018

@author: Ayushi
"""

list1 = input("Enter numbers")        #Read values
list2 = list1.split(",")              #split them into new list
print(list2)                          #print list
print(tuple(list2))                    #convert list into tuple and print it