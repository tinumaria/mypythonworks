#from file in downloads
#age above 50 & country is india
#print fname,lname,age,proff

f=open("C:/Users/tinum/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    if(data[3]>'50' and data[-1]=='india'):
        print(data[1:6])