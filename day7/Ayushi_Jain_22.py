# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:42:10 2018

@author: Ayushi
"""

import oauth2
import time
import urllib
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"  

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="4An2yCQnINz57RC3e3vefArs5", secret="cjyQnI0vX0m6Wtm5noshNqPGY62dUcuwFYwDBVLuC9sgyVgC4O")

token = oauth2.Token(key="3331576618-YI2x6JBO5JB1VWd10p8Pm7FhU4bDI6C10OMfyb7", secret="0HOU4UIe8LG8RjSPY8EKik123a7GwtifKAxJfzbXijsm6")

params["oauth_consumer_key"] = consumer.key

params["oauth_token"] = token.key

params["q"] = "ayushi"


req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib.request.Request(url)

data = json.load(urllib.request.urlopen(response))

filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()
