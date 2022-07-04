#set operation

#1.union
#2.intersection
#3.difference

#1.union - combine 2 sets but duplicated values will not come

st1={1,2,5,8,9,15}
st2={2,5,7,11,14}
st3=st1.union(st2)
print(st3)

#2.intersection - common elements of 2 sets

st1={1,2,5,8,9,15}
st2={2,5,7,11,14}
st3=st1.intersection(st2)
print(st3)

#3.difference - element present in set1 but not present in set2 (a-b)

st1={1,2,5,8,9,15}
st2={2,5,7,11,14}
st3=st1.difference(st2)
print(st3)

st1={1,2,5,8,9,15}
st2={2,5,7,11,14}
st3=st2.difference(st1)
print(st3)


