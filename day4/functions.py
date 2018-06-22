# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:44:56 2018

@author: Ayushi
"""
from functools import reduce

def explain_python():
    """Print a msg explaing what a python is"""
    print("Python is not a snake")
    print("python is a programming language")
    
    
explain_python()



explain_python.__doc__
#in python 2      explain_python.func_doc       #display doc string

"""Filter function"""

def f(x): return x%3 == 0 or x%5 == 0

a = filter(f,range(2,25))
list(a)

"""Map function"""
def cube(x): return x*x*x

b = map(cube,range(1,11))
list(b)

"""reduce function"""

def add(x,y): return x+y

reduce(add,range(1,11))


"""lambda function"""
list(map(lambda x: x*x*x,range(1,11)))



"""Nested List comprehension"""

a=[1,2,3]

[x**2 for x in a]

[x+1 for x in [x**2 for x in a]]



"""length of character"""


words=['it','is','raining','cat','dog']
list(map(lambda x:len(x),words))


