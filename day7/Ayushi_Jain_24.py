# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:18:23 2018

@author: Ayushi
"""


import twitter
api = twitter.Api(consumer_key="4An2yCQnINz57RC3e3vefArs5",consumer_secret="cjyQnI0vX0m6Wtm5noshNqPGY62dUcuwFYwDBVLuC9sgyVgC4O",access_token_key="3331576618-YI2x6JBO5JB1VWd10p8Pm7FhU4bDI6C10OMfyb7",access_token_secret="0HOU4UIe8LG8RjSPY8EKik123a7GwtifKAxJfzbXijsm6")
status = api.PostUpdate("Hello!!")