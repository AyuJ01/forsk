# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:16:16 2018

@author: tanmay
"""

import pandas as pd
df=pd.read_csv("Salaries.csv")
df.head(10)
df.tail()
df.dtypes
df.columns
df.axes
df.ndim
df.values
df.describe
df.max()
df.mean()
df.mode()
df.median()
df.std()
df.sex
df['sex']
df['salary'].count()
df_rank=df.groupby(['rank'])
df_rank.mean()
df.groupby('rank')[['salary']].mean()
df_sub=df[df['salary']>120000]
df_sub[['rank','salary']]
df_f=df[df['sex']=='Female']
df_sub.loc[1:10,['rank','sex','salary']]
df_sub.iloc[1:10,[0,1,2,3]]
df.iloc[[0,5],[1,3]]
df_sorted=df.sort_values(by=['salary','service'],ascending=[True,True])#'doubt'sort to sal se hi ho ra hai
df['salary']=df['salary'].fillna(df['salary'].mean())
df=df.fillna(df.mean())
df[['service','salary']].agg(['mean','max','min'])