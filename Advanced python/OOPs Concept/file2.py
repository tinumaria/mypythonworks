#how to create class

class Person: #person is identifier

#how to create methods in class
#classinte akath define cheyuna function

    def reading(self): #method1  #self is instance keyword
        print("reading book")
    def writing(self): #method2
        print("writing book")

#how to create object

pe=Person() #using class name

#how to create reference

pe.reading() #function call
pe.writing()

#can create multiple object
pe1=Person()
pe1.writing()