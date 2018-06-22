# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:43:37 2018

@author: Ayushi
"""

n = int(input())
l=[]
cmd = []
for i in range(0,n):
    c = input()
    cmd.append(list(c.split(" ")))
    if cmd[-1][0] == "insert":
        index = int(cmd[-1][1])
        value = int(cmd[-1][2])
        l.insert(index,value)
        
    if cmd[-1][0] == "print":
        print(l)
    
    if cmd[-1][0] == "remove":
        value = int(cmd[-1][1])
        l.remove(value)
    
    if cmd[-1][0] == "append":
        value = int(cmd[-1][1])
        l.append(value)
    
    if cmd[-1][0] == "sort":
        l = sorted(l)
        
    
    if cmd[-1][0] == "pop":
        l.pop()
        
    if cmd[-1][0] == "reverse":
        l.reverse()