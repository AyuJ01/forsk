# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:20:58 2018

@author: Ayushi
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    a = student_marks.get(query_name)
    f = sum(a)/len(a)
    f1 = round(f, 2)
    
    print("%.2f" % f)
    
    