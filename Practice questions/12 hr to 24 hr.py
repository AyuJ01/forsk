
str1 = input()
if 'AM' in str1 :
    i = str1.find('AM')
    
    str2 = str1[:i]
    if ord(str1[0])==49 and  ord(str1[1])==50:
        y1 =  chr(ord(str1[0]) - 1)
        y2 =  chr(ord(str1[1]) - 2)
    
    y = str2.replace('12','00',1)
    
    
if 'PM' in str1 :
    i = str1.find('PM')
    
    str2 = str1[:i]
    
    if ord(str2[0])==48 :
        if ord(str2[1])<56:
            y2 =  chr(ord(str1[1]) + 2)        
            y = str2.replace('0','1',1)            
            y = y.replace(str2[1],y2,1)
            
        else:
            y2 =  chr(ord(str1[1]) - 8)                    
            y = str2.replace('0','2',1)
            y = y.replace(str2[1],y2,1)
            
    if ord(str2[0])==49 :
            if ord(str2[1])== 50:
                y=str2
            else:
                
                y2 =  chr(ord(str1[1]) + 2)        
                y = str2.replace('1','2',1)            
                y = y.replace(str2[1],y2,1)
                
print(y)