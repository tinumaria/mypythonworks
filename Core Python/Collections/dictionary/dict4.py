#name,age,prof,sal in dic
#update name to fname
#print prof
#company key present or not
#if not present add company=luminar
#add salary +5000
#print key value pairs seperatly

dic={"name":'tinu',"age":23,"prof":'btech',"sal":10000}

dic["fname"]=dic["name"]
del dic["name"]
print(dic)

print(dic["prof"])

print("company" in dic)
dic["company"]='luminar'

dic["sal"]+=5000

for i in dic:
    print(i,dic[i])