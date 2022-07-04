#create empty list and add 1 to 75 elements
#create even list
#create odd list

#total list sum
#even list sum
#odd list sum

lst=[]
lst_even=[]
lst_odd=[]

for i in range(1,76):
    lst.append(i)
print(lst)

for i in lst:
    if(i%2==0):
        lst_even.append(i)
    else:
        lst_odd.append(i)

print(lst_even)
print(lst_odd)

print(sum(lst))
print(sum(lst_even))
print(sum(lst_odd))
