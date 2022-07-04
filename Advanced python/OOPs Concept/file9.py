#inheritence

#ex: child class collect features of parent class
#class B(child) can use features of class A(parent)

class A:  #parent class, base class, super class
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)
class B(A):  #inheritence  #child class, sub class, derived class
    def printb(self,num2):
        self.num2=num2
        print("inside class B",self.num2,self.num1)
ob=B()
ob.printa(50) #b inherit feature from A class #first printa calleyanam
ob.printb(40)