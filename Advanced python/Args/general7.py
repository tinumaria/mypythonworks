#print subject having lowest marks

dic={
    'physics':56,
    'maths':65,
    'history':80
}
print(dic)
print(min(dic,key=dic.get))



