#word count by removing spcl character

f=open("sample","r")
specl='!@#$%^&*()'
strng=''
for i in f:
    data=i.rstrip("\n")
    for j in data:
        if j not in specl:
            strng+=j
print(strng)

dic={}
data1=strng.split(' ')
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
