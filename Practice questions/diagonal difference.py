# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:56:23 2018

@author: Ayushi
"""

n=int(input())
i=0
lst = []

while i<n:
    lst.append(list(map(int,input().rstrip().split())))
    i+=1
    
#print(lst)
l = len(lst)
sum1=0
sum2=0

a=0
while a<l:
    sum1=sum1+lst[a][a]
    a=a+1
    
print(sum1)
b=0
while l>0:
    sum2 = sum2+lst[b][l-1]
    l-=1
    b+=1
print(sum2)


sumf = abs(sum1-sum2)
print(sumf)