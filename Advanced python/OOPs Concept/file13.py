#multilevel inheritence

class A:
    def printa(self):
        print("inside class A")
class B(A):
    def printb(self):
        print("inside class B")
class C(B):
    def printc(self):
        print("inside class C")
ob=C()
ob.printc()
ob.printa()
ob.printb()

#c inherit b and b inherit a, so all will be printed