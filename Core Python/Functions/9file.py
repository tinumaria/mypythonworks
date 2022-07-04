#find cube of a number

def cube():
    num=int(input("enter a number"))
    cub=num**3
    print(cub)
cube()

#or

def cube(num):
    cub=num**3
    print(cub)
cube(3)

#or

def cube(num):
    cub=num**3
    return cub
data=cube(3)
print(data)
