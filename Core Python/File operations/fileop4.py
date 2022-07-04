lst=[]
lst_even=[]
lst_odd=[]

f=open("sample2","r")
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))

for i in lst:
    if(i%2==0):
        lst_even.append(i)
    else:
        lst_odd.append(i)

print(lst_even)
print(lst_odd)

print(sum(lst_even))
print(sum(lst_odd))


