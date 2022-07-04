#lst=[4,5,10,12,20]
#to
#lst1=[47,46,41,39,31]

#total sum =51
# 51-4
# 51-5
# 51-10
# 51-12
# 51-20

lst=[4,5,10,12,20]
lst1=[]
total=sum(lst)
for i in lst:
    res=total-i
    lst1.append(res)
print(lst1)



