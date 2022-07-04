#tuples

#1.how to define

tu=()   #paranthasis
print(type(tu))

tu1=tuple()
print(type(tu1))

tu=(1,2,3)
print(tu)

#2.heterogenous data supported

tu=(10,10.5,'tinu',True)
print(tu)

#3.duplicated allowed

tu=(10,10,15,15)
print(tu)

#4.insertion order preserved

tu=(10,10.5,'tinu',True)
print(tu)

#5.imutable - cannot update

tu[3]=100
print(tu)

#list & tuple difference
# mutable & immutable

