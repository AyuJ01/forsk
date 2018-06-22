# -*- coding: utf-8 -*-
"""
Created on Tue May 15 00:24:09 2018

@author: Ayushi
"""

list1=input()                 #Read string

list2=list1.split(',')                    #split it into list
list3=list(map(int,list2))                 #convert list into integer
#print(list3)

def add(l):
    a = sum(l)              #calculate sum of list
    return(a)
    

def multiply(l):
    m=1
    for i in l:
        m=m*i                    #multiply list
    return m

def largest(l):
    return max(l)            #find maximum among list

def smallest(l):
    return min(l)            #find minimum among list

def sort(l):
    #a=l.sort
    return(sorted(l))            #sort the list

def remove_duplicates(l):
    return(list(set(l)))           #remove duplicates from the list

def display():
    print("Sum = ",add(list3))
    print("Multiply = ",multiply(list3))
    print("Largest = ",largest(list3))
    print("Smallest = ",smallest(list3))
    print("Sorted = ",sort(list3))
    print("Without Duplicates = ",remove_duplicates(list3))
    
display()                            #call display function