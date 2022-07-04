#multiplication table of a given number
#1*6=6

num=int(input("enter a number"))
i=1
while(i<=10):
    print(i,"*",num,"=",i*num)
    i+=1

#or

num=int(input("enter a number"))
i=1
while(i<=10):
    res=i*num
    print(i,"*",num,"=",res)
    i+=1
