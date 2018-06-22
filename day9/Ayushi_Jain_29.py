# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:18:39 2018

@author: Ayushi
"""

import re



# re.compile converts regex pattern to variable,
# and makes it easier to reuse
regex = re.compile(r'[+-]?\d*[\.][\d]+')

lst = []
## Search 
while True:
    string1 = input()
    if not string1:
        break

# Gets the string from where the match is found
    response = regex.search(string1)
    if response:
        lst.append(True)
    # The groups contain the matched values.
    # It always returns the fully matched string
        #print("True")
    else:
        lst.append(False)
        #print ("False")
        
        
for i in lst:
    print(i)