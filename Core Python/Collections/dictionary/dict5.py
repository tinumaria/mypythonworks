#word count program

line='cat rat bus cat car car rat bus car car bus cat'

#convert line to word by word
#using split

data=line.split(' ')
print(data)

#create empty dic
#if key present in dic, print key=1 else increment

dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
