# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:01:58 2018

@author: Ayushi
"""

import urllib

wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page = urllib.request.urlopen(wiki)

from bs4 import BeautifulSoup as bs

soup = bs(page)

all_tables = soup.find_all('table')

right_table = soup.find('table',class_='table')

A= []
B= []
C= []
D= []
E= []
F= []

for row in right_table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) ==5:
        A.append(cells[0].text.strip())
        B.append((cells[1].text.strip()))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        
        
import pandas as pd

df = pd.DataFrame(A,columns = ['Position'])
df['Team'] = B
df['Matches'] = C
df['Points'] = D
df['Rating'] = E

print(df)
