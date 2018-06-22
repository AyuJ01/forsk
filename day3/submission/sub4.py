string1 = input("Enter the String : ")   #Read string
digit=0             #initialize digit
letter=0            #initialize letter
for element in string1:                #for each element in string
    if element.isdigit():              #if element is digit
       digit+=1                         
    elif(element.isalpha()):            #if element is letter
        letter+=1
        
        #print the values
print("Letters %d"%letter)
print("Digits %d" %digit)                  