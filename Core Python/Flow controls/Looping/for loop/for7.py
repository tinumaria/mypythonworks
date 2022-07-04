#print lower to upper limit even numbers

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
for i in range(low,upp+1):
    if(i%2==0):
       print(i)