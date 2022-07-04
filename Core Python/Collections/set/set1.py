#set

#1.how to define
st=set()  #set function
st={}  #it is dictionary, empty bracket is dictionary
st={1,2,3}  #it is set, values given

#2.heterogenous allowed
st={10,1.5,'tinu'}
print(st)

#3.insertion not preserved
st={10,1.5,'tinu'}
print(st)

#4.duplicated not supported
st={10,10,1.5,'tinu','tinu'}
print(st)

st={2,3,True}
print(st)
st={1,2,3,True}  #True value is 1 #duplicated not allowed
print(st)

#5.mutable

