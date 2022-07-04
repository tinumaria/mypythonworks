#map & filter
#............

#map - output for every element
#lst=[1,2,3,4,5,6]   f(x)=[1,2,3,4,5,6]

#filter - output for element satisfying condition
#f(x)=[2,4,6]

#syntax:
#variable_name=list(map(arguement1,arguement2))
#variable_name=list(filter(arguement1,arguement2))

#arguement1-function
#arguement2-iterable

#map
#square of number
lst=[1,2,3,4,5,6]
def square(num):
    res=num**2
    return res
data=list(map(square,lst))
print(data)

#again we can reduce using lambda
data=list(map(lambda num:num**2,lst))
print(data)

#filter
#even number
lst1=[1,2,3,4,5,6]
def even(num):
    return num%2==0
data=list(filter(even,lst))
print(data)

#again we can reduce using lambda
data=list(filter(lambda num:num%2==0,lst))
print(data)

