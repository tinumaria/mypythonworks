#method overloading
#same method name & different no. of arguement

#2 class Add(num1,num2) & Add1(num1,num2,num3)

class Add:
    def sum(self,num1,num2):  #2 arguement
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add1(Add):
    def sum(self,num1,num2,num3):  #3 arguement
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)
ob=Add1()
ob.sum(5,6,7)

#only 2nd method(Add1) will work
#python wont support method overloading, latest method(Add1) will work in python
