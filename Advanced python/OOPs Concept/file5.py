#class - employee
#attribute - name,id,design,salary,company

class Employee:
    def setvalue(self,name,id,design,sal,comp):
        self.name=name
        self.id=id
        self.design=design
        self.sal=sal
        self.comp=comp
    def printvalue(self):
        print(self.name,self.id,self.design,self.sal,self.comp)

pe1=Employee()
pe1.setvalue("tinu",45,"django",20000,"luminar")
pe1.printvalue()
