#collect fname of student with highest mark

student=[('anu',30),('vinay',45),('arjun',35),('vipin',36)]

marks=[]

for i in student:
    marks.append(i[1])

maximum=max(marks)
print(maximum)

for j in student:
    if j[1]==maximum:
        print(j[0])

