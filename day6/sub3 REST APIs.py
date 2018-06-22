"""
import urllib
f= urllib.request.urlopen("http://13.127.155.43/api_v0.1/sending")
"""



import requests
#r = requests.urllib3.get_host("http://13.127.155.43/api_v0.1/sending")
#r+="?q=Phone_Number"

d = {   
         'Phone_Number' : '7894561230',
         'Name' : 'Ayushi',
         'College_Name' : 'PIET',
         'Branch' : 'CS'
    }

resp = requests.post("http://13.127.155.43/api_v0.1/sending",json = d)
print (resp.text)

url = "http://13.127.155.43/api_v0.1/receiving"
url += "?Phone_Number=7894561230"

r = requests.get(url)
print(r.text)



"""
#Method 2

import requests
import json
#r = requests.urllib3.get_host("http://13.127.155.43/api_v0.1/sending")
#r+="?q=Phone_Number"

d = {   
         'Phone_Number' : "7894561230",
         'Name' : 'Ayushi',
         'College_Name' : 'PIET',
         'Branch' : 'CSE'
    }
d = json.dumps(d)
resp = requests.post("http://13.127.155.43/api_v0.1/sending",data = d,headers={"Content-Type":"application/json"})
print (resp.text)

url = "http://13.127.155.43/api_v0.1/receiving"
url += "?Phone_Number=7894561230"

r = requests.get(url)
print(r.text)


"""