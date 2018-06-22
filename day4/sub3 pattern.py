# -*- coding: utf-8 -*-
"""
Created on Tue May 15 00:31:58 2018

@author: Ayushi
"""
k=0
num=int(input())            #Read input
for i in range(1,2*(num+1)):
    if i<=num:
        k=k+1
    else:
        k=k-1
    #print(i)
    for j in range(1,k+1):
        #print(j)
        print("*",sep=' ',end=' ',flush='True')                    #print pattern
    print("")
    
