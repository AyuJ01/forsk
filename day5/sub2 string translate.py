str11=input()

def translate(str1):
    vowel="aeiou "
    ch=0    
    str2=""
    while(ch<len(str1)):
        if str1[ch] in vowel:
            str2=str2+str1[ch]
            ch=ch+1
        else:
            str2= str2+str1[ch]+"o"+str1[ch]
            ch=ch+1
    
    return str2
    
print(translate(str11))
"""
Approach 2
vol = 'aeiouAEIOU '
print (''.join(i+"o"+i if i not in vol else i for i in str11))
"""

"""
approach 3
lst=[]
for i in str11:
    if i in vol:
       lst.append(i)
    else:
        lst.append(i+"o"+i)
print (''.join(lst))

"""






