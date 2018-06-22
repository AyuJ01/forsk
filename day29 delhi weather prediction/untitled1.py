# -*- coding: utf-8 -*-

import urllib

#///----------------------
#----------Gurgaon ------------

w_gur = "https://www.worldweatheronline.com/gurgaon-weather-history/haryana/in.aspx"

page = urllib.request.urlopen(w_gur)

from bs4 import BeautifulSoup as bs

soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')


#--time--
tim=[]

tim_div = soup.find_all('div',class_='tb_row tb_date')
for j in range(0,9):
    a = tim_div[j].find_all('div',class_='tb_cont_item')
    
    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(":")
        
        tim.append(int(cell[0]))


#--temp--
tem_gur=[]

tem_div = soup.find_all('div',class_='tb_row tb_temp')
for j in range(0,9):
    a = tem_div[j].find_all('div',class_='tb_cont_item')
    
    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        tem_gur.append(int(cell[0]))

#--wind--

wind_div = soup.find_all('div',class_='tb_row tb_wind')

wind_gur=[]
for j in range(0,9):
    a = wind_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        wind_gur.append(int(cell[0]))

#--humidity--
hum_div = soup.find_all('div',class_='tb_row tb_humidity')

hum_gur=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        hum_gur.append(int(cell[0]))


#--pressure--
pres_div = soup.find_all('div',class_='tb_row tb_pressure')
#a = pres_div.findAll('div',class_='tb_cont_item')

pres_gur=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        pres_gur.append(int(cell[0]))


    
#--------------//

#///----------------------
#----------Delhi ------------

w_del = "https://www.worldweatheronline.com/delhi-weather-history/delhi/in.aspx"

page = urllib.request.urlopen(w_del)

soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')


#--temp--
tem_del=[]

tem_div = soup.find_all('div',class_='tb_row tb_temp')
for j in range(0,9):
    a = tem_div[j].find_all('div',class_='tb_cont_item')
    
    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        tem_del.append(int(cell[0]))

#--wind--

wind_div = soup.find_all('div',class_='tb_row tb_wind')

wind_del=[]
for j in range(0,9):
    a = wind_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        wind_del.append(int(cell[0]))

#--humidity--
hum_div = soup.find_all('div',class_='tb_row tb_humidity')

hum_del=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        hum_del.append(int(cell[0]))


#--pressure--
pres_div = soup.find_all('div',class_='tb_row tb_pressure')
#a = pres_div.findAll('div',class_='tb_cont_item')

pres_del=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        pres_del.append(int(cell[0]))



#--------------//

#///----------------------
#----------Noida ------------

w_noi = "https://www.worldweatheronline.com/noida-weather-history/uttar-pradesh/in.aspx"

page = urllib.request.urlopen(w_noi)


soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')

#--temp--S
tem_noi=[]

tem_div = soup.find_all('div',class_='tb_row tb_temp')
for j in range(0,9):
    a = tem_div[j].find_all('div',class_='tb_cont_item')
    
    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        tem_noi.append(int(cell[0]))

#--wind--

wind_div = soup.find_all('div',class_='tb_row tb_wind')

wind_noi=[]
for j in range(0,9):
    a = wind_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        wind_noi.append(int(cell[0]))

#--humidity--
hum_div = soup.find_all('div',class_='tb_row tb_humidity')

hum_noi=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        hum_noi.append(int(cell[0]))


#--pressure--
pres_div = soup.find_all('div',class_='tb_row tb_pressure')
#a = pres_div.findAll('div',class_='tb_cont_item')

pres_noi=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        pres_noi.append(int(cell[0]))




#--------------//
#----------Ghaziabad ------------

w_noi = "https://www.worldweatheronline.com/ghaziabad-weather-history/uttar-pradesh/in.aspx"

page = urllib.request.urlopen(w_noi)

soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')

#--temp--
tem_gha=[]

tem_div = soup.find_all('div',class_='tb_row tb_temp')
for j in range(0,9):
    a = tem_div[j].find_all('div',class_='tb_cont_item')
    
    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        tem_gha.append(int(cell[0]))

#--wind--

wind_div = soup.find_all('div',class_='tb_row tb_wind')

wind_gha=[]
for j in range(0,9):
    a = wind_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split(" ")
        
        wind_gha.append(int(cell[0]))

#--humidity--
hum_div = soup.find_all('div',class_='tb_row tb_humidity')

hum_gha=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        hum_gha.append(int(cell[0]))


#--pressure--
pres_div = soup.find_all('div',class_='tb_row tb_pressure')
#a = pres_div.findAll('div',class_='tb_cont_item')

pres_gha=[]
for j in range(0,9):
    a = hum_div[j].find_all('div',class_='tb_cont_item')

    for i in range(1,len(a)):
        
        cel = a[i].text
        cell = cel.split("%")
        
        pres_gha.append(int(cell[0]))


#--------------//


            
        
import pandas as pd

df = pd.DataFrame(tim,columns = ['Time'])
df['Temp_Gurgaon'] = tem_gur
df['Wind_Gurgaon'] = wind_gur
df['Humidity_Gurgaon'] = hum_gur
df['Pressure_Gurgaon'] = pres_gur

df['Temp_Noida'] = tem_noi
df['Wind_Noida'] = wind_noi
df['Humidity_Noida'] = hum_noi
df['Pressure_Noida'] = pres_noi


df['Temp_Ghaziabad'] = tem_gha
df['Wind_Ghaziabad'] = wind_gha
df['Humidity_Ghaziabad'] = hum_gha
df['Pressure_Ghaziabad'] = pres_gha


df['Temp_Delhi'] = tem_del
df['Wind_Delhi'] = wind_del
df['Humidity_Delhi'] = hum_del
df['Pressure_Delhi'] = pres_del

#[12,39,3,25,999,38,3,25,999,37,3,27,999]
#print(df)


features = df.iloc[:,:-4].values
labels = df.iloc[:,-4:].values


#splitting the dataset
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


#LinearRegression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)
pred = regressor.predict(features_test)


score = regressor.score(features_test,labels_test)
import numpy as np
val = np.array([39,3,25,999,38,3,25,999,37,3,27,999]).reshape(1,-1)

val2 = np.array([3,37,8,38,995,37,5,37,995,36,4,40,995]).reshape(1,-1)

pred2 = regressor.predict(val2)

pred1 = regressor.predict(val)
