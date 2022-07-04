st={10,20,30,40,50,60,70,80,90,100}
print(st)

#remove function - delete function
st.remove(30)
print(st)

#discard function
st.discard(50)
print(st)

#difference betn remove & discard
# remove has return type
# discard has no return type

st.remove(150)  # keyword not present
print(st)
st.discard(150)  # will print st
print(st)