# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:11:52 2018

@author: Ayushi
"""

string1 = input("Enter the String")                     #Read the string


dict1={}                                               #initialize an empty dictionary
for element in string1:                                #for each element in string1
    if element in dict1.keys():                        #if element is already present in the dictionary
        dict1[element]+=1                              #then increase its value
    else:                                              #else if element is not present 
        dict1[element]=1                               #then add it to dictionary with value 1
        
        
print(dict1)                                           #print dictionary