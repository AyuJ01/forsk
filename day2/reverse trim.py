# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:44:01 2018

@author: Ayushi
"""

str1=input('input: ')
str2=str1.strip()
b=str2.find(" ")

#s1=str2[b:].strip()
#s2=str2[:b].strip()

print("%s %s" %(str2[b:].strip(),str2[:b].strip()))

