#1. create a list from element of a range from 1200 to 2000 with step of 130
#2. lst1=[44,54,64,74,104] and create new list as lst2=[50,60,70,80,110]
#3. create 1 to 15 element list and print data of elements square greater than 50

#1.
lst=[i for i in range(1200,2000,130)]
print(lst)

#2.
lst1=[44,54,64,74,104]
lst2=[i+6 for i in lst1]
print(lst2)

#3.
lst=[i for i in range(1,16) if i**2>50]
print(lst)