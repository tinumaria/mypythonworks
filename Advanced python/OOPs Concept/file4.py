#class - student
#atribute - name,rollno,dept,college

class Student:
    def setvalue(self,name,roll,dept,clge):
        self.name=name
        self.roll=roll
        self.dept=dept
        self.clge=clge
    def printvalue(self):
        print(self.name,self.roll,self.dept,self.clge)

pe1=Student()
pe1.setvalue("tinu",45,"CE","christ")
pe1.printvalue()

pe2=Student()
pe2.setvalue("san",38,"CE","christ")
pe2.printvalue()