# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:04:25 2018

@author: Ayushi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:18:39 2018

@author: Ayushi
"""

import re



# re.compile converts regex pattern to variable,
# and makes it easier to reuse


lst = []
## Search  
regex = re.compile(r'^[456](\d{15}| \d{3}(-\d{4}){3})')

while True:
    string1 = input()
    if not string1:
        break

    lst.append(string1)
    
    
for i in lst:
    response = regex.match(i)
    conti = re.search(r"(\d)\1{4,}", i.replace('-',''))

    if response and not conti:
        print("Valid")
    else:
        print ("Invalid")

