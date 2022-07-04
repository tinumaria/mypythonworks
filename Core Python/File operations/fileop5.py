#word count from another sample

f=open("sample3","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(' ')
    for i in data:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
print(dic)

#print key value pairs
for i in dic:
    print(i,":",dic[i])

#or using items function
for k,v in dic.items():
    print(k,":",v)