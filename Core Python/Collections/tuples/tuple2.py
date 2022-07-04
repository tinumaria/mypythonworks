tu=(30,40,50,60,70)
print(tu)

#update 50 to 100
#tuple is immutable
#convert tuple to list

lst=list(tu)
lst[2]=100
print(lst)

tu=tuple(lst)
print(tu)
