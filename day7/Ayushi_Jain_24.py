# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:18:23 2018

@author: Ayushi
"""


import twitter
api = twitter.Api(consumer_key="CONSUMER_KEY",consumer_secret="CONSUMER_SECRET",access_token_key="TOKEN_KEY",access_token_secret="TOKEN_SECRET")
status = api.PostUpdate("Hello!!")
