#List Slicing

lst=[2,5,7,8,6,4,15,12,20,17]
print(lst[1:4])

#Positive indexing

#firstvalue=1
#endvalue=3
#lst[1],lst[2],lst[3]

print(lst[3:8])
print(lst[:7])  #lst[0] to lst[6]
print(lst[3:])  #lst[3] to end of list
print(lst[:])   #full list

#Negative indexing

#-1 to -n
#starts from end

print(lst[-1])
print(lst[-6])
print(lst[-4:-1])  #from lst[-4] to lst[-2]
print(lst[-3:])    #from lst[-3] to lst[-1]
print(lst[:-4])    #from lst[-n] to lst[-5] #travel from begining only

print(lst[-2:-5])  #will not work
