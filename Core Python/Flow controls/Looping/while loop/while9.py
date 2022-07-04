#reverse a number in output
#153 - 351  #1234 - 4321

#153%10=3   #153//10=15

#15%10=5    #15//10=1

#1%10=1

num=int(input("enter a number")) #153
res=0
while(num!=0): #153!=0
     dig=num%10  #dig=153%10=3  #dig=15%10=5
     res=(res*10)+dig  #res=0*10+3=3  #res=3*10+5=35
     num=num//10  #num=153//10=15  #num=15//10=1
print(res)