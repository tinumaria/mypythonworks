#factorial
#5 :1*2*3*4*5

def factorial():
    num=int(input("enter a number"))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)
factorial()

#or

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)
factorial(5)

#or

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
data=factorial(5)
print(data)


