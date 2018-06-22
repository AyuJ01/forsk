# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:26:47 2018

@author: Ayushi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:00:57 2018

@author: Ayushi
"""

import pandas as pd


from sklearn.preprocessing import LabelEncoder
#Read csv
df=pd.read_csv("Automobile.csv")

#print datatypes
for i in df.columns:
    print(i,df[i].dtype)

#new dataframe where datatype = object
df_new = df.select_dtypes(object)


#missing data handling

df_new[df_new.isnull().any(axis=1)]
df_new["num_doors"].value_counts()


df_new = df_new.fillna({"num_doors" : "four"})

#label encoding in body_style

labelencoder = LabelEncoder()

df_new["body_style"] = labelencoder.fit_transform(df_new["body_style"])

#one hot encoding

df_new = pd.get_dummies(df_new, columns=['drive_wheels'])

df_new = pd.get_dummies(df_new, columns=['body_style'])



