#multiple inheritence with constructor

#class 1 - person(name,age,place)
#class 2 - employee(id,dept,sal)
#class 3 - student(roll,clg)
#student inherit person & emploee

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee:
    def __init__(self,dept,sal):
        self.dept=dept
        self.sal=sal
class student(person,employee):
    def __init__(self,roll,clg,name,age,dept,sal):
        person.__init__(self,name,age)  #class name used to call constructor in multiple inheritence
        employee.__init__(self,dept,sal)
        self.roll=roll
        self.clg=clg
    def print(self):
        print(self.name,self.age,self.dept,self.sal,self.roll,self.clg)

ob=student("tinu",23,"python",25000,101,"luminar")
ob.print()

#output not in order

#single inheritence - super(), child class & parent arguements

#multiple inheritence - class name