#dictionary

#1.how to define
dic={}
print(type(dic))

#key value pairs
dic={"roll":101,"name":'tinu',"age":23,"dept":'python',"salary":10000}
print(dic)

#2.heterogenous data supported
dic={"roll":101,"name":'tinu',"age":23,"dept":'python',"marks":40.5}
print(dic)

#3.duplicated value supported, duplicated key not supported
dic={"roll":101,"name":'tinu',"age":23,"dept":'python',"marks":23}
print(dic)

dic={"roll":101,"name":'tinu',"age":23,"dept":'python',"age":23}
print(dic)

#4.insertion order preserved
#print in same order

#5.mutable
