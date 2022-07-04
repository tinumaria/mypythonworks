num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

try:
    print(num1/num2)
except Exception as e:
    print("exception occured",e)

