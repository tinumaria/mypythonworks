#input no. of classes held, no.of classes attended, print perecentage of class attended
#student will not be allowed to sit in exam if his/her attendance is less than 75%

held=int(input("number of classes held"))
attended=int(input("number of classes attended"))
percent=(attended/held)*100
print(percent)
if(percent>75):
    print("you are allowed to sit for exam",)
else:
    print("you are not eligibe")