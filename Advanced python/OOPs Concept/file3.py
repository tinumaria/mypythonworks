#how to create arguements in method

class Person:
    def setvalue(self,name,age,place):  #oru funtionle value vere functionil useyan patila
        self.fname=name  #self keyword is to change entered arguement to instance arguement
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.fname)
        print(self.age)
        print(self.place)
pe1=Person()
pe1.setvalue("tinu",23,"thrissur")
pe1.printvalue()

pe2=Person()
pe2.setvalue("san",19,"thrissur")
pe2.printvalue()

