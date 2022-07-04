#mutable - update value

dic={"roll":101,"name":'tinu',"age":23,"dept":'python',"marks":50}
print(dic)

#value collected using key
print(dic["marks"])
print(dic["name"])

#update value 50 to 30
dic["marks"]=30
dic["name"]='sandra'
print(dic)

#or
dic["marks"]+=20
print(dic)

#to add new key:value
dic["total"]=150
print(dic)

#to delete key:value
del dic["roll"]
print(dic)