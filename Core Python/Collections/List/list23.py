#print pairs of list

lst=[4,3,2,1]
num=int(input("enter a number"))
for i in lst:
    for j in lst:
        if(i+j==num):
            print(i,j,end=' ')

#or

lst1=[4,3,2,1]
num1=int(input("enter a number"))
low=0
upp=len(lst1)-1

while(low<=upp):
    data=lst1[low]+lst1[upp]
    if(data==num1):
        print("pairs are",lst1[low],lst1[upp])
        break
    elif(data>num1):
        upp=upp-1
    else:
        low=low+1

