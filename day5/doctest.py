# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:16:30 2018

@author: Ayushi
"""
import doctest
def Add(p,q):
    """
    Perform Addition
    >>> Add(12,3)
    15
    >>> Add(4,5)
    9
    """
    return p*q
doctest.testmod()