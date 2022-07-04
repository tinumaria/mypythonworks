master_string="abbcddeghgggt"
check_word="egg"

res=""
dic={}

for i in master_string:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

for i in check_word:
    if i in dic:
        count=dic.get(i)
        if count>0:
            res+=i
            dic[i]-=1
        else:
            break
    else:
        break

print(res==check_word)
