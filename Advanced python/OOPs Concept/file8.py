#constructor

#to define instance variable in object
#__init__

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)

pe1=Person("tinu",23,"ijk")
pe1.printvalue()