
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:21:24 2018

@author: Ayushi
"""

import urllib

#///----------------------
#----------Gurgaon ------------

w_gur = "https://www.worldweatheronline.com/gurgaon-weather-history/haryana/in.aspx"

page = urllib.request.urlopen(w_gur)

from bs4 import BeautifulSoup as bs

soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')

#--time--
tim_div = soup.find('div',class_='tb_row tb_date')
a = tim_div.findAll('div',class_='tb_cont_item')

tim=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(":")
    
    #s = cells.text
    tim.append(int(cell[0]))


#--temp--
tem_div = soup.find('div',class_='tb_row tb_temp')
a = tem_div.findAll('div',class_='tb_cont_item')

tem_gur=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    tem_gur.append(int(cell[0]))

#--wind--
wind_div = soup.find('div',class_='tb_row tb_wind')
a = wind_div.findAll('div',class_='tb_cont_item')

wind_gur=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    wind_gur.append(int(cell[0]))

#--humidity--
hum_div = soup.find('div',class_='tb_row tb_humidity')
a = hum_div.findAll('div',class_='tb_cont_item')

hum_gur=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split("%")
    
    #s = cells.text
    hum_gur.append(int(cell[0]))

#--pressure--
pres_div = soup.find('div',class_='tb_row tb_pressure')
a = pres_div.findAll('div',class_='tb_cont_item')

pres_gur=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    pres_gur.append(int(cell[0]))

    
#--------------//

#///----------------------
#----------Delhi ------------

w_del = "https://www.worldweatheronline.com/delhi-weather-history/delhi/in.aspx"

page = urllib.request.urlopen(w_del)

soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')


#--temp--
tem_div = soup.find('div',class_='tb_row tb_temp')
a = tem_div.findAll('div',class_='tb_cont_item')

tem_del=[]
for i in range(1,9):
    
    cel = a[i].text
    cell = cel.split(" ")
    
    tem_del.append(int(cell[0]))



#--wind--
wind_div = soup.find('div',class_='tb_row tb_wind')
a = wind_div.findAll('div',class_='tb_cont_item')

wind_del=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    wind_del.append(int(cell[0]))

#--humidity--
hum_div = soup.find('div',class_='tb_row tb_humidity')
a = hum_div.findAll('div',class_='tb_cont_item')

hum_del=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split("%")
    
    #s = cells.text
    hum_del.append(int(cell[0]))

#--pressure--
pres_div = soup.find('div',class_='tb_row tb_pressure')
a = pres_div.findAll('div',class_='tb_cont_item')

pres_del=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    pres_del.append(int(cell[0]))



#--------------//

#///----------------------
#----------Noida ------------

w_noi = "https://www.worldweatheronline.com/noida-weather-history/uttar-pradesh/in.aspx"

page = urllib.request.urlopen(w_noi)


soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')


#--temp--
tem_div = soup.find('div',class_='tb_row tb_temp')
a = tem_div.findAll('div',class_='tb_cont_item')

tem_noi=[]
for i in range(1,9):
    
    cel = a[i].text
    cell = cel.split(" ")
    
    tem_noi.append(int(cell[0]))


#--wind--
wind_div = soup.find('div',class_='tb_row tb_wind')
a = wind_div.findAll('div',class_='tb_cont_item')

wind_noi=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    wind_noi.append(int(cell[0]))

#--humidity--
hum_div = soup.find('div',class_='tb_row tb_humidity')
a = hum_div.findAll('div',class_='tb_cont_item')

hum_noi=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split("%")
    
    #s = cells.text
    hum_noi.append(int(cell[0]))

#--pressure--
pres_div = soup.find('div',class_='tb_row tb_pressure')
a = pres_div.findAll('div',class_='tb_cont_item')

pres_noi=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    pres_noi.append(int(cell[0]))




#--------------//
#----------Ghaziabad ------------

w_noi = "https://www.worldweatheronline.com/ghaziabad-weather-history/uttar-pradesh/in.aspx"

page = urllib.request.urlopen(w_noi)

soup = bs(page)

all_div = soup.find_all('div',class_='tb_content')


#--temp--
tem_div = soup.find('div',class_='tb_row tb_temp')
a = tem_div.findAll('div',class_='tb_cont_item')

tem_gha=[]
for i in range(1,9):
    
    cel = a[i].text
    cell = cel.split(" ")
    
    tem_gha.append(int(cell[0]))
    

#--wind--
wind_div = soup.find('div',class_='tb_row tb_wind')
a = wind_div.findAll('div',class_='tb_cont_item')

wind_gha=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
    wind_gha.append(int(cell[0]))

#--humidity--
hum_div = soup.find('div',class_='tb_row tb_humidity')
a = hum_div.findAll('div',class_='tb_cont_item')

hum_gha=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split("%")
    
    #s = cells.text
    hum_gha.append(int(cell[0]))

#--pressure--
pres_div = soup.find('div',class_='tb_row tb_pressure')
a = pres_div.findAll('div',class_='tb_cont_item')

pres_gha=[]
for i in range(1,9):
    
    #print(row)
    cel = a[i].text
    cell = cel.split(" ")
    
    #s = cells.text
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



