#read a string from console
#remove vowels
#add balance letters to string

strng1=input("enter a string")
strng2=''
vowels='aeiouAEIOU'
for i in strng1:
    if i not in vowels:
        strng2+=i
print(strng2)
