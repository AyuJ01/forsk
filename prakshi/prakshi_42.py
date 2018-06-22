# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:42:22 2018

@author: tanmay
"""

import urllib.request
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
page=urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table',class_='wikitable')
A=[]
B=[]
for row in right_table.findAll("tr"):
    cells=row.findAll('td')
    if(len(cells)==7):
        A.append(str(cells[1].text.strip()))
        B.append(str(cells[4].text.strip()))
import pandas as pd
df=pd.DataFrame(A,columns=['State'])

df['National_Share']=B

print(df.head(6))                

#import numpy as np
import matplotlib.pyplot as plt
labels=A[0:6]
sizes=B[0:6]

exp = [0.2,0,0,0,0,0] #0.2 tells the space which we have to drop from all sides to take one part here
  #Raj out and give rest arg as 0
ax1 = plt.subplot()
ax1.pie(sizes, labels=labels, autopct='%1.2f%%',explode=exp)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.