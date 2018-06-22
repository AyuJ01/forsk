
str1=input()
def reverse(s1):
    s2=""
    l=len(s1)
    i=l
    while(i!=0):
        s2=s2+s1[i-1]
        i=i-1
    return s2
    

print(reverse(str1))




print(str1[::-1])



"""
s2=""
l=len(s1)
i=l
while(i!=0):
    s2=s2+s1[i-1]
    i=i-1
    
print(s2)

"""