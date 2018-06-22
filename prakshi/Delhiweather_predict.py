# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:03:09 2018

@author: tanmay
"""

import urllib.request
#airport_location=['VIDP','VOHS','VIDD','']
#for air in airport_location:
url="https://www.wunderground.com/history/airport/VIDP/2018/6/20/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo="
page=urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table',{'id':'obsTable'}) #name of class from where body starts see only body code ignore heading
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in right_table.findAll("tr"):
    cells=row.findAll('td')
    #states=row.findAll('th')
    if cells!=[]:
        A.append(str(cells[0].text.strip()))
        B.append(str(cells[2].text.strip()))
        C.append(str(cells[5].text.strip()))
        D.append(str(cells[8].text.strip()))
        E.append(str(cells[11].text.strip()))
        F.append(str(cells[14].text.strip()))
        G.append(str(cells[17].text.strip()))
        
      

import pandas as pd

df=pd.DataFrame(A,columns=['June'])

df['Temp']=B
df['Dew point']=C
df['Humidity']=D
df['sea level pressure']=E

df['Visibility']=F

df['Wind']=G

print(df)   

labels_train=df


#2nd city  
import urllib.request
#airport_location=['VIDP','VOHS','VIDD','']
#for air in airport_location:
url="https://www.wunderground.com/history/airport/VOHS/2018/6/20/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo="
page=urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table',{'id':'obsTable'}) #name of class from where body starts see only body code ignore heading
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in right_table.findAll("tr"):
    cells=row.findAll('td')
    #states=row.findAll('th')
    if cells!=[]:
        A.append(str(cells[0].text.strip()))
        B.append(str(cells[2].text.strip()))
        C.append(str(cells[5].text.strip()))
        D.append(str(cells[8].text.strip()))
        E.append(str(cells[11].text.strip()))
        F.append(str(cells[14].text.strip()))
        G.append(str(cells[17].text.strip()))

import pandas as pd

df=pd.DataFrame(A,columns=['June'])

df['Temp']=B
df['Dew point']=C
df['Humidity']=D
df['sea level pressure']=E

df['Visibility']=F

df['Wind']=G

features_train=df




#city3
import urllib.request
#airport_location=['VIDP','VOHS','VIDD','']
#for air in airport_location:
url="https://www.wunderground.com/history/airport/VIDD/2018/6/20/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo="
page=urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table',{'id':'obsTable'}) #name of class from where body starts see only body code ignore heading
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in right_table.findAll("tr"):
    cells=row.findAll('td')
    #states=row.findAll('th')
    if cells!=[]:
        A.append(str(cells[0].text.strip()))
        B.append(str(cells[2].text.strip()))
        C.append(str(cells[5].text.strip()))
        D.append(str(cells[8].text.strip()))
        E.append(str(cells[11].text.strip()))
        F.append(str(cells[14].text.strip()))
        G.append(str(cells[17].text.strip()))
        
        

import pandas as pd

features_train['June1']=A
features_train['Temp1']=B
features_train['Dew point1']=C
features_train['Humidity1']=D
features_train['sea level pressure1']=E

features_train['Visibility1']=F

features_train['Wind1']=G


#city4
import urllib.request
#airport_location=['VIDP','VOHS','VIDD','']
#for air in airport_location:
url="https://www.wunderground.com/history/airport/VEPB/2018/6/20/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo="
page=urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table',{'id':'obsTable'}) #name of class from where body starts see only body code ignore heading
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in right_table.findAll("tr"):
    cells=row.findAll('td')
    #states=row.findAll('th')
    if cells!=[]:
        A.append(str(cells[0].text.strip()))
        B.append(str(cells[2].text.strip()))
        C.append(str(cells[5].text.strip()))
        D.append(str(cells[8].text.strip()))
        E.append(str(cells[11].text.strip()))
        F.append(str(cells[14].text.strip()))
        G.append(str(cells[17].text.strip()))
        
        

import pandas as pd

features_train['June2']=A
features_train['Temp2']=B
features_train['Dew point2']=C
features_train['Humidity2']=D
features_train['sea level pressure2']=E

features_train['Visibility22']=F

features_train['Wind2']=G



features_train=features_train.drop(features_train.index[0])


















