# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:37:35 2018

@author: Ayushi
"""

fp = open("text.txt")
type(fp)

fp.read()
print(fp.read())

fp.close()

fp = open("text.txt")
fp.readline()

fp.readlines()

#fp.seek(offset, from_what)

fp.seek(0, 1)       #error
   #1: from current position   #2:from end of the file    #0: beginning of the file
fp.readline()

for line in fp:
    print(line)


fp.close()

fp = open("text.txt",'w')
fp.write("machine learning clasS")
fp.close()