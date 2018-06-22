# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:00:29 2018

@author: KARIS
"""
 
# open weather api: ff1246fde51147b9eb2b662f6e613121


#new delhi ,gurgaon,  gurugram , faridabad , noida, ghaziabad,panipat, sonipat,patparganj, burari

import urllib.request
url = "https://www.wunderground.com/history/airport/VIDP/2018/6/16/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo="
page = urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")
right_table = soup.find('table',{'id':'obsTable'})

DateDel = []
TempDel= []
DewPointDel= []
HumiditypercentDel= []
SeaLevelDel= []
VisiblityDel = []
WindDel = []
rows = right_table.find_all("tr")
for row in rows:
    
    cells = row.findAll('td')
    if len(cells)==21:
        DateDel.append(cells[0].text.strip())
        TempDel.append(cells[2].text.strip())
        DewPointDel.append(cells[5].text.strip())
        HumiditypercentDel.append(cells[8].text.strip())
        SeaLevelDel.append(cells[11].text.strip())
        VisiblityDel.append(cells[14].text.strip())
        WindDel.append(cells[17].text.strip())
import pandas as pd
labels = pd.DataFrame(DateDel,columns=['DateDel'])
labels['TempDel']=TempDel
labels['HumiditypercentDel']=HumiditypercentDel
labels['SeaLevelDel'] = SeaLevelDel
labels['VisiblityDel']= VisiblityDel
labels["WindDel"] = WindDel
labels.drop(labels.index[0],inplace = True, axis = 0)


fariurl = "https://www.wunderground.com/history/airport/VOHS/2018/6/20/MonthlyHistory.html?req_city=VOHS&req_statename=India&reqdb.zip=00000&reqdb.magic=242&reqdb.wmo=WVOHS"
page = urllib.request.urlopen(fariurl)

soup = BeautifulSoup(page, "lxml")
right_table = soup.find('table',{'id':'obsTable'})

DateFari = []
TempFari= []
DewPointFari= []
HumiditypercentFari= []
SeaLevelFari= []
VisiblityFari = []
WindFari = []
rows = right_table.find_all("tr")
for row in rows:
    
    cells = row.findAll('td')
    if len(cells)==21:
        DateFari.append(cells[0].text.strip())
        TempFari.append(cells[2].text.strip())
        DewPointFari.append(cells[5].text.strip())
        HumiditypercentFari.append(cells[8].text.strip())
        SeaLevelFari.append(cells[11].text.strip())
        VisiblityFari.append(cells[14].text.strip())
        WindFari.append(cells[17].text.strip())
import pandas as pd
feat = pd.DataFrame(DateFari,columns=['DateFari'])
feat['TempFari']=TempFari
feat['HumiditypercentFari']=HumiditypercentFari
feat['SeaLevelFari'] = SeaLevelFari
feat['VisiblityFari']= VisiblityFari
feat["WindFari"] = WindFari



ghazurl = "https://www.wunderground.com/history/airport/VIDD/2018/6/20/MonthlyHistory.html?req_city=Safdarjung&req_state=DL&req_statename=India&reqdb.zip=00000&reqdb.magic=70&reqdb.wmo=42182"
page = urllib.request.urlopen(ghazurl)

soup = BeautifulSoup(page, "lxml")
right_table = soup.find('table',{'id':'obsTable'})

DateGhaz = []
TempGhaz= []
DewPointGhaz= []
HumiditypercentGhaz= []
SeaLevelGhaz= []
VisiblityGhaz = []
WindGhaz = []
rows = right_table.find_all("tr")
for row in rows:
    
    cells = row.findAll('td')
    if len(cells)==21:
        DateGhaz.append(cells[0].text.strip())
        TempGhaz.append(cells[2].text.strip())
        DewPointGhaz.append(cells[5].text.strip())
        HumiditypercentGhaz.append(cells[8].text.strip())
        SeaLevelGhaz.append(cells[11].text.strip())
        VisiblityGhaz.append(cells[14].text.strip())
        WindGhaz.append(cells[17].text.strip())
import pandas as pd
feat['DateGhaz']=DateGhaz
feat['TempGhaz']=TempGhaz
feat['HumiditypercentGhaz']=HumiditypercentGhaz
feat['SeaLevelGhaz'] = SeaLevelGhaz
feat['VisiblityGhaz']= VisiblityGhaz
feat["WindGhaz"] = WindGhaz
feat.drop(feat.index[0],inplace = True, axis = 0)

from sklearn.model_selection import train_test_split as TTS
feat_train, feat_test , labels_train , labels_test = TTS(feat , labels ,test_size = 0.2 ,random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
feat_train = sc.fit_transform(feat_train)
feat_test = sc.transform(feat_test)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(feat_train , labels_train)
labels_pred = regressor.predict(feat_test)

Score = regressor.score(feat_test, labels_test)
