#class 1 - Person
#attribute - name,age
#class 2 - Child
#attribute - place,school
#class 3 - Student
#attribute - roll,dept,college
#print name,age,place,dept,college using multilevel

class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setchild(self,place,school):
        self.place=place
        self.school=school
class Student(Child):
    def setstudent(self,roll,dept,clg):
        self.roll=roll
        self.dept=dept
        self.clg=clg
    def printstudent(self):
        print(self.name,self.age,self.place,self.dept,self.clg)
st=Student()
st.setperson("tinu",23)
st.setchild("ijk","DB")
st.setstudent(101,"civil","christ")
st.printstudent()