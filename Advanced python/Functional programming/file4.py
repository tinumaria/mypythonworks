#list comprehension
#..................

#create empty list, add 1 to 100 element
lst=[]
for i in range(1,101):
    lst.append(i)
print(lst)

#to make list program in single step - list comprehension

#syntax 1:
#.........
#lst=[print range]

#add 1 to 100
lst=[i for i in range(1,101)]
print(lst)

#add 1 to 75 and print(1,5,9,13,17,21....75)
lst=[i for i in range(1,76,4)]
print(lst)

#syntax 2:
#.........
#lst=[print range condition]

#add 1 to 100 elements and print even numbers
lst=[i for i in range(1,101) if i%2==0]
print(lst)

#add 1 to 50 elements and print odd numbers
lst=[i for i in range(1,51) if i%2!=0]  #or i%2==1
print(lst)

#add 1 to 50 elements and print even if number is even
lst=[(i,"even") for i in range(1,51) if i%2==0]
print(lst)

#syntax 3:
#.........
#lst=[print1 if condition else print2 range]
#lst=[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range]

#add 1 to 50 elements and print square if even or print cube if odd
lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

#add 1 to 50 elements and print square if even or print that number if odd
lst=[i**2 if i%2==0 else i for i in range(1,51)]
print(lst)

lst=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
print(lst)

#add 1 to 30 elements and print even and number if even or print odd and number if odd
lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,31)]
print(lst)

#add 1 to 50 elements and print square if even or print 0 if divisible by 5 or print number if odd
lst=[i**2 if i%2==0 else 0 if i%5==0 else i for i in range(1,31)]
print(lst)

