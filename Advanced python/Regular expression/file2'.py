import re
s='daddydaaadyddadaday'
count=0
matcher=re.finditer('da',s)
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)