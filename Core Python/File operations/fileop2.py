#Read operation

#if both file in same package
f=open("sample1","r")
for i in f:  #will work only in loop
    print(i)

#if both file in different package
f=open("C:/Users/tinum/pycharmProjects/april_python_django/File operations/sample1","r")  #use / in filepath
for i in f:
    print(i)