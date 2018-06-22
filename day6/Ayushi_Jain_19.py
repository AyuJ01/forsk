alpha = "abcdefghijklmnopqrstuvwxyz "           
str1= input().lower()                         #Read input and convert it into lower case
flag=0                                        #set the flag value to 0
for ch in alpha:                              #for each character in alphabet
    if ch not in str1:                        #if any alphabet is not present in string
        flag=1                                 #then set flag = 1
        break                                   #terminate the for loop

if flag==0:                                       
    print("PANGRAM")
else:
    print("NOT PANGRAM")