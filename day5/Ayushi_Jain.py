import PIL
#Read Image Convert it into greyscale and rotate 90 degree clockwise
img_filename = PIL.Image.open("sample.jpg").convert('L').rotate(-90)     
#img_filename.show()    

w = img_filename.size[0] / 2
h = img_filename.size[1] / 2
size = (w-80,h-102,w+80,h+102)
img_filename=  img_filename.crop(size)           #crop image from center of (width=160,height=204)

s=(75,75)
img_filename.thumbnail(s)                       #make thumbnail
img_filename.show()
