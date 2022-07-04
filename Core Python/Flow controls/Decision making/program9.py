#read 2 number from console, print largest number with if ..elif...else

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

if(num1>num2):
    print("largest number is",num1)
elif(num2>num1):
    print("largest number is",num2)
else:
    print("both numbers are same")

