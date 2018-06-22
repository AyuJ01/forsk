# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:04:59 2018

@author: Ayushi
"""

import PIL
img= PIL.Image.open('sample.jpg')

w = int(img.size[0] / 2)
h = int(img.size[1] / 2)
size = (w-80,h-102,w+80,h+102)


#box = (100, 100, 400, 400)
region = img.crop(size)
region = region.transpose(PIL.Image.ROTATE_180)
img.paste(region, size)
img.show()






url="http://"
import requests
resp= requests.get(url)
print(resp.text)