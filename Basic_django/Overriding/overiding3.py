class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    def __str__(self):
        return self.course_name

class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.name=kwargs.get("name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.name

dj=Course()
dj.add_course(course_name="django",status=True)
print(dj)
ms=Course()
ms.add_course(course_name="mearnstack",status=True)

djb1=Batch()
djb1.add_batch(course=dj,batch_code="djangoapril22",start_date="20-4-22")
print(djb1)
msb1=Batch()
msb1.add_batch(course=ms,batch_code="mearnstackapril22",start_date="20-4-22")

st1=Student()
st1.add_student(name="tinu",email="tinu@gmail.com",batch=djb1)
st2=Student()
st2.add_student(name="siva",email="siva@gmail.com",batch=djb1)
st3=Student()
st3.add_student(name="steewo",email="steewo@gmail.com",batch=djb1)

st4=Student()
st4.add_student(name="san",email="san@gmail.com",batch=msb1)
st5=Student()
st5.add_student(name="sandra",email="sandra@gmail.com",batch=msb1)

print(st1)
print(st1.batch)
print(st4)
print(st4.batch)

#print all students in list

students=[]
students.append(st1)
students.append(st2)
students.append(st3)
students.append(st4)
students.append(st5)

#print students in mearnstack

ms_stud=[stud.name for stud in students if stud.batch.course.course_name=="mearnstack"]
print(ms_stud)