# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:19:10 2018

@author: Ayushi
"""


import pandas as pd

df=pd.read_csv("Loan.csv")
df = df.drop("Loan_ID",axis=1)


for i in df.columns:
    if df[i].dtype == object:
        df[i] = df[i].astype('category')
        df[i] = df[i].cat.codes


df = pd.get_dummies(df, columns=['Property_Area'])

#%%



