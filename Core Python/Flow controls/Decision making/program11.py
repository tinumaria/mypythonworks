#largest among 3 numbers

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))

if(num1>num2>num3):
    print("largest number is",num1)
elif(num2>num1>num3):
    print("largest number is",num2)
else:
    print("largest number is",num3)

#or

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))

if(num1>num2)&(num1>num3):
    print("largest number is",num1)
elif(num2>num1)&(num2>num3):
    print("largest number is",num2)
else:
    print("largest number is",num3)
