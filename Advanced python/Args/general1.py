#*args - to read multiple values

#2 numbers
def printvalue(num1,num2):
    print(num1,num2)
printvalue(5,9,10)  #only 2 numbers can be read

#to read multiple numbers
def printvalue(*args):
    print(args)  #in tuple format
printvalue(5,9,10)  #will read all numbers