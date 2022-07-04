#from file in downloads

f=open("C:/Users/tinum/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    print(data)
    #print fname,lname,age
    print(data[1:4])  #or print(data[1],[2],[3])
    print(data[0:5:2])  #2 is step (index0,index2,index4 will print)