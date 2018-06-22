import datetime
import requests
pn = input("Enter Phone no. : ")
msg = input("Enter Message : ")

resp = requests.post("https://smsapi.engineeringtgr.com/send/?Mobile=7597476620&Password=prashita&Message="+msg+"&To="+pn+"&Key=ayushg49aiK70dkrIzcnRo")

print (resp.text)

#post data into mlab
myAPIKey = "7FInsrG0SeZEwVZGYjsrA9jegtt9e9xi"
#Url 
url = "https://api.mlab.com/api/1/databases/db_university/collections/reg?apiKey="+myAPIKey


data={
      "mob_no":pn,
      "sms":msg,
      "Date-Time":str(datetime.datetime.now())
      
      }
r=requests.post(url,json= data) #sending data on server and in parameter we send
                               #url and data in json format    
                             
print(r.text) 