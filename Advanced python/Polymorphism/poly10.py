#read customer file from downloads using constructor
#id,fname,lname,age,proff,loc

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
    loc=data[-1] #if we put 5, list out of range

    ob=person(id,fname,lname,age,prof,loc)
    ob.print()

    #if we need only fname & lname
    print(ob.fname,ob.lname)
