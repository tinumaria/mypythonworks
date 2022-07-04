# read lower and upper limit
# print prime number between low & upp

low=int(input("enter a lower limit"))
upp=int(input("enter a upper limit"))
flag=0
for i in range(low,upp):
     if(num%i==0):
        flag=1
        break
if(flag>0):
    print(num)

    