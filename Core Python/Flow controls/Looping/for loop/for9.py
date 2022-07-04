#read lower limit & upper limit
#print even sum & odd sum

low=int(input("enter a lower limit"))
upp=int(input("enter upper limit"))
sum_even=0
sum_odd=0
for i in range(low,upp+1):
    if(i%2==0):
      sum_even+=i
    else:
        sum_odd+=i
print(sum_even)
print(sum_odd)