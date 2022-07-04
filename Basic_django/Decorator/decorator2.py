#to call multiple values use *args & **kwargs
#give (self,*args,**kwargs) instead of (self,user,role)

def admin_permission(fn):
    def innerfn(*args,**kwargs):
        user=kwargs.get("user")
        if user.role!="admin":
            raise Exception("permission denied")
        else:
            return fn(*args,**kwargs)
    return innerfn

class User:
    def setuser(self,username,role):
        self.username=username
        self.role=role
    def printuser(self):
        print(self.username,self.role)

class Addcourse:
    @admin_permission
    def setcourse(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.coursename=kwargs.get("coursename")
    def printcourse(self):
        print(self.coursename)

class Addbatch:
    @admin_permission
    def setbatch(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.course=kwargs.get("course")
        self.batchname=kwargs.get("batchname")
    def printbatch(self):
        print(self.batchname)

user1=User()
user1.setuser("tinu","admin")

course1=Addcourse()
course1.setcourse(user=user1,coursename="django")

batch1=Addbatch()
batch1.setbatch(user=user1,course=course1,batchname="april")

course1.printcourse()
batch1.printbatch()