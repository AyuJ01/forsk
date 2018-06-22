

alpha = "abcdefghijklmnopqrstuvwxyz "
str1= input().lower()
flag=0
for ch in alpha:
    if ch not in str1:
        flag=1
        break

if flag==0:
    print("PANGRAM")
else:
    print("NOT PANGRAM")