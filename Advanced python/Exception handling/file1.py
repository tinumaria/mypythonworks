#Exception handling
#..................

num1=int(input("enter number 1")) #6
num2=int(input("enter number 2")) #0
print(num1/num2) #6/0 - unexpected error

#to handle unexpected input errors

#3 blocks:
#try : exception veran chance olla code add in try block
#except : solution add in except block
#finally : will work if exception is there or not

num3=int(input("enter number 3")) #6
num4=int(input("enter number 4")) #0

try:
    print(num3/num4)
except:
    print("zero division error") #no error #will display zero division error
finally:
    print("good")

