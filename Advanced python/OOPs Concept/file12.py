#class 1 - Person
#attribute - name,age
#class 2 - Parent
#attribute - place, phone no.
#class 3 - Employee
#attribute - id, designation, salary

class Person:
    def printa(self,name,age): # self or this  can be used
        self.name=name
        self.age=age
class Parent:
    def printb(self,place,phone):
        self.place=place
        self.phone=phone
class Employee(Person,Parent):
    def printc(self,id,desig,sal):
        self.id=id
        self.desig=desig
        self.sal=sal
        print(self.name,self.age,self.place,self.phone,self.id,self.desig,self.sal)
ob=Employee()
ob.printa("tinu",23)
ob.printb("ijk",9747130704)
ob.printc(101,"python",20000)

#or

class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Parent:
    def setparent(self,place,phone):
        self.place=place
        self.phone=phone
class Employee(Person,Parent):
    def setemployee(self,id,desig,sal):
        self.id=id
        self.desig=desig
        self.sal=sal
    def printemployee(self):
        print(self.name,self.age,self.place,self.phone,self.id,self.desig,self.sal)
emp=Employee()
emp.setperson("tinu",23)
emp.setparent("ijk",9747130704)
emp.setemployee(101,"python",20000)
emp.printemployee()
