# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:28:58 2018

@author: Ayushi
"""

if __name__ == '__main__':
    ln=[]
    ls=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ln.append(name)
        ls.append(score)
        
    mins = min(ls)
    #ind_maxs = ls.index(maxs)
    
    val=max(ls)
    #len(arr)

    for i in range(0,len(ls)):
        #if val!=maxi:
            if ls[i]<val and ls[i]!=mins:
                val = ls[i]

    index_list = []
    for k in range(0,len(ls)):
        if val == ls[k]:
            index_list.append(k)
    
    name_list=[]
    for n in index_list:
        
        name_list.append(ln[n])
        
    name_l = sorted(name_list)
    for a in name_l:
        print(a)