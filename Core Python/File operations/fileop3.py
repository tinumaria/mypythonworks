lst=[]
f=open("sample2","r")
for i in f:  #will work only in loop
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))

#\n in output - for every new line \n will come
#rstrip function is used to remove \n

# line=hello\n

# data=line.rstrip("\n")
# print(data)
# output is hello

# data=line.rstrip("o\n")
# print(data)
# output is hell