# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:30:39 2018

@author: Ayushi
"""

import facebook as fb
import PIL

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBAJKJQ4ZBUi8sPnoGp040fUuTVVQmgzAyEZACOEVHvr7joJcZBFMP9tgQrBiuYwzittnCwp3ky3nABZBIyrtBtby54on9Lle8CTVXTAQyjeEvAuLKDEAZCd0cB1XUYSUNoOM1evrSF8kCB91SdL9w7NHGWDbU5GiM5XGcEd3s9JwM4pe5pML8a5uMZBXEFZBIgZDZD"

# Message to post as status on Facebook
status = "Hello..!!"

# Authenticating
graph = fb.GraphAPI(access_token)

# Posting Status on your wall
post_id = graph.put_wall_post(status)


img = PIL.Image.open("img2.jpg")

post_id1 = graph.put_photo(image = open('k.jpg','rb'),message = "Memories :-* ")
post_id = graph.put_wall_post(img)

#photo = open("img2.jpg", "rb")
#graph.put_object("me","photos",message="hell", source=photo.read())
#photo.close()
