#read element from console
#elemnt found
#element not found

#Linear search

lst=[1,5,7,8,3,6,7,15,20]
num=int(input("enter number"))
for i in lst:
    if(i==num):
        print("element found")
        break
else:
    print("element not found")

#or

lst1=[1,5,7,8,3,6,7,15,20]
num1=int(input("enter number"))
if num1 in lst1:
    print("element found")
else:
    print("element not found")

#Drawback
#time consuming
#complexity increases