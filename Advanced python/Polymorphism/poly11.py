#read customer file from downloads using constructor
#append fname,lname,age,proff to list

class person:
    def __init__(self,id,fname,lname,age,prof,loc):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.loc=loc
    def print(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.loc)

f=open("C:/Users/tinum/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(',')
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    loc=data[-1]

    ob=person(id,fname,lname,age,prof,loc)
    lst=[]
    lst.append((ob.fname,ob.lname,ob.age,ob.prof))
    print(lst)
