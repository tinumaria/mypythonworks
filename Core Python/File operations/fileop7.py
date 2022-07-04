#from file in downloads
#age above 50
#print fname,lname,age,proff

f=open("C:/Users/tinum/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    if(data[3]>'50'):
        print(data[1:5])

