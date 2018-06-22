#Using requests and json library
import requests
import urllib         
import json
#define dictionary
data = {   
         'Phone_Number' : "7894561230",
         'Name' : 'Ayushi Jain',
         'College_Name' : 'PIET',
         'Branch' : 'CSE'
    }
#convert json data into dictionary format
d = json.dumps(data)


####
"""
data1 ={   
         'Phone_Number' : "1234567890",
         'Name' : 'Ayushi',
         'College_Name' : 'PIET',
         'Branch' : 'CS'
    } 


data1 = bytes( urllib.parse.urlencode( data1 ).encode() )
handler = urllib.request.urlopen( "http://13.127.155.43/api_v0.1/sending", data1 )
print( handler.read().decode( 'utf-8' ) )

import json

data = json.dumps(data1)
header = {"Content-Type":"application/json"}
req =  urllib.request.Request("http://13.127.155.43/api_v0.1/sending", data=data,headers=header) # this will make the method "POST"
resp = urllib.request.urlopen(req)
print(resp.read().decode( 'utf-8' ))
###

"""
#Post request to REST API url


resp = requests.post("http://13.127.155.43/api_v0.1/sending",data = d,headers={"Content-Type":"application/json"})
print (resp.text)              #print the server response

#REST API url
url = "http://13.127.155.43/api_v0.1/receiving"
url += "?Phone_Number=7894561230"

r = requests.get(url)            #get request to REST API
print(r.text)                    #print the server response

