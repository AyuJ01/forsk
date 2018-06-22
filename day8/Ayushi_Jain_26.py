

from collections import OrderedDict
dd = OrderedDict()
while True:
    str1 = input()
    if not str1:
        break
    
    str2 = str1[::-1]
    
    tup1 = str2.split(' ',1)
    
    t0 = str(tup1[0])
    t0= int(t0[::-1])
    
    t1 = str(tup1[1])
    t1= t1[::-1]
    
    if t1 in dd:
        dd[t1] = dd[t1]+t0
    else:
        dd[t1]=t0
    
    
for k,v in dd.items():
    print(k,v)
    

