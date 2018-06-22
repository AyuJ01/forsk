# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:45:52 2018

@author: Ayushi
"""

#import Libraries
import json
import requests

#API KEY
myAPIKey = "7FInsrG0SeZEwVZGYjsrA9jegtt9e9xi"
#Url 
url = "https://api.mlab.com/api/1/databases/db_university/collections/reg?apiKey="+myAPIKey


data = {   
                "Student Name" : 'Ayushi',
                "Student Age" : '18',
                "Student Roll_no" : '1',
                "Student Branch" : 'CS'
       }
#convert json data into dictionary format
d = json.dumps(data)

#Post the data into url
resp = requests.post(url,data = d,headers={"Content-Type":"application/json"})

print (resp.text)


