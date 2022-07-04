#add value

lst=[]
print(lst)

#append function
#add element to empty list
#at a time single element

lst.append(10)
lst.append(50)
lst.append('python')
print(lst)

#extend function
#at a time multiple elements
#add at end part

lst.extend([10,20,30]) #square bracket inside normal bracket
print(lst)

#insert function
#to add element in middle or exact position

lst.insert(1,150)
print(lst)

lst.insert(5,'django')
print(lst)
