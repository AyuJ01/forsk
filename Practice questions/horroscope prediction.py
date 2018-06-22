# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:08:08 2018

@author: Ayushi
"""


import urllib
sign='0'
sun = input("Enter your zodiac sign: ").lower()

if sun== "aries":
    sign='1'
if sun == "taurus":
    sign='2'
elif sun== "gemini":
    sign='3'
elif sun== "cancer":
    sign='4'
elif sun== "leo":
    sign='5'
elif sun== "virgo":
    sign='6'
elif sun== "libra":
    sign='7'
elif sun== "scorpio":
    sign='8'
elif sun== "sagittarius":
    sign='9'
elif sun== "capricorn":
    sign='10'
elif sun== "aquarius":
    sign='11'
elif sun== "pisces":
    sign='12'




hor = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="+sign

page = urllib.request.urlopen(hor)

from bs4 import BeautifulSoup as bs

soup = bs(page)

all_para = soup.find_all('div')
right_para = soup.find('div',class_='horoscope-content')

A= []
        
p= right_para.find("p")
    
A.append(p.text.strip())
        

s = ''.join(A)
print(s)



import twitter
api = twitter.Api(consumer_key="4An2yCQnINz57RC3e3vefArs5",consumer_secret="cjyQnI0vX0m6Wtm5noshNqPGY62dUcuwFYwDBVLuC9sgyVgC4O",access_token_key="3331576618-YI2x6JBO5JB1VWd10p8Pm7FhU4bDI6C10OMfyb7",access_token_secret="0HOU4UIe8LG8RjSPY8EKik123a7GwtifKAxJfzbXijsm6")
st = api.PostUpdates(s)