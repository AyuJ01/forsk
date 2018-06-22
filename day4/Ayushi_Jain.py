
dict1={}                                   #initialize an empty dictionary
keys=['a','b','c']                         #assign the keys

#Read input
dict1['a']=int(input("Enter element a : "))
dict1['b']=int(input("Enter element b : "))
dict1['c']=int(input("Enter element c : "))

#Calculate the sum of values if they are not teen(13,19) or if they are 15 and 16
def fix_teen(dict1):
    count=0
    for num in dict1.values():    
        if num in range(13,20):
            if num==15 or num==16:
                count=count+num
            else:
                count=count+0
        else:
            count=count+num
    
    return count
print ("Sum = ",fix_teen(dict1))

