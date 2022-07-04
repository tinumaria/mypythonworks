#given number is prime or not
#2,3,5,7,11,13

num1=int(input("enter a number 1"))
flag=0
for i in range(2,num1):
    if(num1%i==0):
        flag=1
        break
if(flag>0):
    print(num1,"is not prime")
else:
    print(num1,"is prime")

#or

num2=int(input("enter a number 2"))

for i in range(2,num2):
    if(num2%i==0):
       print(num2,"is not prime")
       break
else:
    print(num2,"is prime")
