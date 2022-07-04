#nested list

lst=[[101,'tinu','t',23,'python',1000],
     [102,'sinu','u',24,'bigdata',1500],
     [103,'minu','v',25,'python',2000],
     [104,'vinu','w',26,'python',2500],
     [105,'jinu','x',27,'bigdata',3000],
     [106,'finu','y',28,'python',3500]]

for i in lst:
     print(i)

#from fname to proff

for i in lst:
     print(i[1:5])

for i in lst:
     print(i[1],i[2],i[3],i[4])

#age above 25

for i in lst:
     if(i[3]>25):
          print(i[1:5])

#working in bigdata

for i in lst:
     if(i[4]=='bigdata'):
          print(i[1],i[2],i[3],i[5])

#salary above 1750 and age above 25

for i in lst:
     if(i[3]>25)&(i[5]>2600):
          print(i[1:6])

#total salary

sum=0
for i in lst:
     sum+=i[5]
print(sum)
