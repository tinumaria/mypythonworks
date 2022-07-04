#program to accept cost price of a bike & display road tax to be paid according to
#cost price       tax
#>100000          15%
#>50000&<=100000  10%
#<=50000          5%

cost=int(input("enter cost of bike"))
tax=0
if(cost>100000):
    print("tax=",cost*15/100)
elif(50000<cost<=100000): #elif(cost>50000)&(cost<=100000)
    print("tax=",cost*10/100)
else:
    print("tax=",cost*5/100)