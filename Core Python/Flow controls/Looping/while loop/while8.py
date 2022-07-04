#read lower limit & upper limit
#print even sum & odd sum

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
i=low
sum_even=0
sum_odd=0
while(i<=upp):
     if(i%2==0):
        sum_even+=i
     else:
        sum_odd+=i
    i+=1
print(sum_even)
print(sum_odd)
