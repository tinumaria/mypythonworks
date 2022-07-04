#Binary search

#list create
#sort list in ascending order

#declare 2 variables
#low=0
#upp=len(lst)-1

#calculate mid
#mid=(low+upp)//2

#check 3 conditions
#1. search element > lst[mid]
#    low=mid+1
#2. search element < lst[mid]
#    upp=mid-1
#3. search element = lst[mid]
#    element found

lst=[1,5,7,8,3,6,7,15,20]
lst.sort()
print(lst)
num=int(input("enter search element"))
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")





