# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:58:45 2018

@author: Ayushi
"""


flag = 0
count=1
str1 = input()
tup1 = str1.split(' ')
l = list(map(int,tup1))    
for i in l:
    if i<0:
        break
    
    a= str(i)
    if a == a[::-1]:
        #count +=1
        flag = 1
            
    
if(flag==0):
    print("False")
    
else:
    #if(count==len(l)):
     #   print("True")
    #else:
        print("True")

