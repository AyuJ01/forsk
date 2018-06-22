# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:30:47 2018

@author: tanmay
"""

import pandas as pd
df=pd.read_csv("Automobile.csv")
df['price']=df['price'].fillna(df['price'].mean())
price=df['price'].values
print(min(price))
print(max(price))
print(price.mean())
print(price.std())
