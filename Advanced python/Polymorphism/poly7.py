#single inheritance with constructor

#class 1 - Person(name,age,place)
#class 2 - Student(roll,dept,clg)
#student inherit person

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Student(Person):
    def __init__(self,roll,dept,clg,name,age,place):
        super().__init__(name,age,place)  #super used to call constructor in single inheritence
        self.roll=roll
        self.dept=dept
        self.clg=clg
    def printstu(self):
        print(self.roll,self.dept,self.clg,self.name,self.age,self.place)

ob=Student("tinu",23,"ijk",101,"python","luminar")
ob.printstu()
