# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:43:50 2018

@author: tanmay
"""
#import urllib
import requests
import datetime
mob_no=input("Enter mobile no")
msg=input("Enter msg")
url="http://sms.dataoxytech.com/index.php/smsapi/httpapi/?uname=sylvester007&password=forskmnit&sender=FORSKT&receiver="+mob_no+"&route=TA&msgtype=1&sms="+msg
#url="http://sms.dataoxytech.com/index.php/smsapi/httpapi/?uname=sylvester007&password=forskmnit&sender=FORSKT&receiver=8107960588&route=TA&msgtype=1&sms=Hello"
resp=requests.get(url)
print(resp.text)

myAPI="bwLk-Y4Uz4pbL-N6NFc2edSqCt0R1GGe"
url1= "https://api.mlab.com/api/1/databases/db_sms/collections/mob_sms?apiKey="+myAPI
#req=urllib.request.urlopen(url)
#print(req)
data={
      "mob_no":mob_no,
      "sms":msg,
      "Date-Time":str(datetime.datetime.now())
      
      }
r=requests.post(url1,json= data) #sending data on server and in parameter we send
                               #url and data in json format    
                             
print(r.text) 



