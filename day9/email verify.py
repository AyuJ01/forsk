# -*- coding: utf-8 -*-S
"""
Created on Tue May 22 11:47:38 2018

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
regex = re.compile(r'[a-zA-Z0-9_-]+[@][a-zA-Z0-9]+[\.][a-zA-Z]{2,4}$')

lst = []
## Search 
while True:
    string1 = input()
    if not string1:
        break

# Gets the string from where the match is found
    response = regex.match(string1)
    if response:
    # The groups contain the matched values.
    # It always returns the fully matched string
        lst.append(string1)
    
    
print(lst)