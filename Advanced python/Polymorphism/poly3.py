#method overriding
#same method name & same no of arguement

#2 class Add(num1,num2) & Add2(no1,no2)

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class A",self.num1+self.num2)
class Add2(Add):
    def sum(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print("inside class B",self.no1+self.no2)
ob=Add2()
ob.sum(15,20)

#child class(Add2) will execute, child class will override parent class

