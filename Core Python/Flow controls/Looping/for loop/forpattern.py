for i in range(1,4): #i=1,2
    for j in range(1,4): #j=1,2
        print(i)
#output in single line downward
# 1
# 1
# 1
# 2
# 2
# 2
# 3

for i in range(1,4):
    for j in range(1,4):
        print(i,end='')
#output in same line
#1 1 1 2 2 2 3 3 3

for i in range(1,4):
    for j in range(1,4):
        print(i,end='')
    print()
#output
# 1 1 1
# 2 2 2
# 3 3 3
