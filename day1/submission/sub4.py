str=input("Enter string: ")        #Read string
a=str.split()                      #split the string with space
a=a[::-1]                          #reverse the list
print(' '.join(a))                   #join the list
