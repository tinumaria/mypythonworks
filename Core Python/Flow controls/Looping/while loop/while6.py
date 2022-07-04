#print even numbers between lower & upper limit

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
i=low
while(i<=upp):
    if(i%2==0):
      print(i)
    i+=1