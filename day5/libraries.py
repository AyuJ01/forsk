# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:58:23 2018

@author: Ayushi
"""

#for zip the content
import zlib
s="abcdef djffdkf sdnwiu s dad wejef ds,kaf  fkj gk gkreger . Fmwem fjk mju  j   e rgjh d ehf m gl  g. rtg gr r rewnj ir.Fnndf df dfgvgnog dfg."
len(s)
#t = zlib.compress(s)   # error: a bytes-like object is required, not 'str'
t = zlib.compress(s.encode("ascii"))
zlib.decompress(t)


#to read the content of website
import urllib
 #urllib.urlopen("http://www.forsk.in")     in py2
#f = urllib.request("http://www.forsk.in")       #error: 'module' object is not callable
f= urllib.request.urlopen("http://www.forsk.in")
f.read(1000)


#
import os
os.getcwd()


#image processing  //python image library
#import PIL
from PIL import Image
from PIL import ImageFilter
img_filename = Image.open("sample1.png")
img_filename.show()

img_filename.filter(ImageFilter.BLUR).show()
img_filename.mode   #A for transparancy