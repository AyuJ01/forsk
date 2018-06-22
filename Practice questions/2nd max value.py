# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:05:18 2018

@author: Ayushi
"""

arr = list(map(int, input().split()))
maxi = max(arr)
val=min(arr)
len(arr)

for i in range(0,len(arr)):
    #if val!=maxi:
        if arr[i]>val and arr[i]!=maxi:
            val = arr[i]
            
print(val)

