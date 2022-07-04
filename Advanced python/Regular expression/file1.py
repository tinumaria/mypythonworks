#Regular expression

#python package
#pattern matching

import re
s="abaaaaabbabaaabab"
count=0

#finditer (can pass only 2 arguement)

#arguement 1 - find pattern (find cheyanda data)
#arguement 2 - string name

matcher=re.finditer('ab',s)
#if do print(matcher), location will be printed, so iterate

for i in matcher:
    count+=1
    print(i.group())  #to get ab
    print(i.start())  #to get index
print(count)

