# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:52:35 2018

@author: Ayushi
"""

"""
small=int(input("Enter the no. of small bricks : "))
large=int(input("Enter the no. of large bricks : "))
target=int(input("Enter the target value : "))
"""

l=input()
l1=l.split(",")
l2=list(map(int,l1))

small=l2[0]
large=l2[1]
target=l2[2]

l,s=divmod(target,5)
if(l<=large):
    if(s<=small):
        print("true")
    else:
        print("False")
else:
    print("False")
    
    
    
    
    
"""
if(((small*1)+(large*5))>=target):
    print("True")
else:
    print("False")
    
    """