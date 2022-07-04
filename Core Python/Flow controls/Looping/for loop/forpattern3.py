#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')  #if pattern is same value print i #if pattern is different value print j
    print()