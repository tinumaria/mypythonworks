#read 3 numbers from console
#find second largest number with nested if

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))

if(num1>num2)&(num1>num3): #num1 is largest
    if(num2>num3):
       print("second largest number is",num2)
    else:
        print("second largest number is",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
       print("second largest number is",num1)
    else:
        print("second largest number is",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
       print("second largest number is",num1)
    else:
        print("second largest number is",num2)
else:
    print("invalid")
