#create a list
#add even numbers to new list

lst1=[10,11,12,15,16,17,20,21,22,25,26,27,30,31,32]
lst2=[]
for i in lst1:
    if(i%2==0):
        lst2.append(i)
print(lst2)

