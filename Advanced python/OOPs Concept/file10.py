#create 2 class - Person(name,age,place), Student(roll,dept)
#last print name age place roll dept

class Person:
    def printp(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Student(Person):
    def prints(self,roll,dept):
        self.roll=roll
        self.dept=dept
        print(self.name,self.age,self.place,self.roll,self.dept)

s=Student()
s.printp("tinu",23,"ijk")
s.prints(101,"python")

