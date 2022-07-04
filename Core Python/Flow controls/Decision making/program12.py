#read 4 subject mark
#print grade of student from total marks

sub1=int(input("enter first subject mark"))
sub2=int(input("enter second subject mark"))
sub3=int(input("enter third subject mark"))
sub4=int(input("enter forth subject mark"))
total=sub1+sub2+sub3+sub4

if(total>=180):
    print("grade is A+")
elif(total>=160)&(total<=179): #(160<=total<=179)
    print("grade is A")
elif(total>=140)&(total<=159):
    print("grade is B+")
elif(total>=120)&(total<=139):
    print("grade is B")
elif(total>=100)&(total<=119):
    print("grade is C+")
elif(total>=80)&(total<=99):
    print("grade is C")
else:
    print("fail")


