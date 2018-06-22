# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:07:10 2018

@author: Ayushi
"""
lst=[]
while True:
    l=[]

    str1 = input()
    if not str1:
        break
    
    n1 = str1.find('@')
    n2 = str1.find('.')
    
    s = str1[0 : n1]
    
    s1 = str1[n1+1:n2]
    
    s2 = str1[n2+1:]
    
    for ch in s:
        
        if ch.isalnum()  or ch =='_' or ch =='-':
            l.append(ch)
            
    a = ''.join(l)
    
    if a==s:
    
        if s1.isalnum():
            if(len(s2)<4 and len(s2)>0):
            
                lst.append(str1)
    
print(lst)


    