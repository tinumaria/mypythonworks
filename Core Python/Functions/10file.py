#create calculator
#print
#1. addition
#2. substraction
#3. multiplication
#4. division

#enter your choice
#read num1 & num2

def add():
    sum=num1+num2
    print(sum)
def subs():
    minus=num1-num2
    print(minus)
def mult():
    multiply=num1*num2
    print(multiply)
def div():
    divide=num1/num2
    print(divide)

print("1.Addition\n"
      "2.Substraction\n"
      "3.Multiplication\n"
      "4.Division")

choice=int(input("enter your choice"))
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

if(choice==1):
    add()
elif(choice==2):
    subs()
elif(choice==3):
    mult()
elif(choice==4):
    div()
else:
    print("invalid")

#or

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("1.Addition\n"
      "2.Substraction\n"
      "3.Multiplication\n"
      "4.Division")

choice=int(input("enter your choice"))
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

if(choice==1):
    print(num1,"+",num2,"=",add(num1,num2)
elif(choice==2):
    print(num1,"-",num2,"=",sub(num1,num2)
elif(choice==3):
    print(num1,"*",num2,"=",mul(num1,num2)
elif(choice==4):
    print(num1,"/",num2,"=",div(num1,num2)
else:
    print("invalid")


