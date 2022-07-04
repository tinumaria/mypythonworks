# create a file and add some content
# copy it to new file using write

f=open("sample4","r")
f1 = open("write_data1", "w")
for i in f:
    f1.write(i)
