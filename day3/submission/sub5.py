# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:30:34 2018

@author: Ayushi
"""


list1=input("enter values separated by ',' : ")                 #Read string
list2=list1.split(',')                                          #Convert it into list
list3=list(map(int,list2))                                       #convert the value of list into integer
print(list3)
small=min(list3)                                                #select the minimum value from list
large=max(list3)                                                #select the maximum value from list
list3.remove(small)                                             #Remove the smallest element from list
list3.remove(large)                                             #Remove the largest element from the list
#count=sum(list3)
print(sum(list3)/len(list3))                                     #calculate the average value

"""flag=0
for i in list3:
    flag=flag+i
    
flag2=flag/(len(list3))
print(flag2)
"""
