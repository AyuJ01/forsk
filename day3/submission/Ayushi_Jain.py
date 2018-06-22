# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:11:22 2018

@author: Ayushi
"""

list1=input("enter values separated by ',' : ")               #Read Values
list2=list1.split(',')                                        #split them into new list
list3=list(map(int,list2))                                    #convert the values in list into int 
#print(list3)                              

count=0
flag=0
for item in list3:
    flag+=1                                                   #increment the value of flag
    if item==13:                                          
        flag=0          
    
    if flag==0 or flag==1:
        count=count
    else:
        count=count+item                                     #calculate the sum 
    #print(flag)   
print(count)
    
    