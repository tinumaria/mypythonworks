#can read and print in one method

class Add:
    def setnumber(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
sum=Add()
sum.setnumber(40,50)