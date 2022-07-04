#static variable

#it is used when a variable has common value ie. every student has same college name
#so college is static variable not instance variable
#static variable is called by class name

#class name - luminar
#attribute - name,roll,age,institution,fees

class Luminar:
    institution="luminartechnolab"
    fees=25000
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,Luminar.institution,Luminar.fees)

s1=Luminar()
s1.setvalue("tinu",45,23)
s1.printvalue()

s2=Luminar()
s2.setvalue("siva",38,24)
s2.printvalue()

s3=Luminar()
s3.setvalue("steewo",42,24)
s3.printvalue()