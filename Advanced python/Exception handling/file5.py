#Generate Exception

age=int(input("enter your age"))
if(age>=18):
    print("eligible")
else:
    raise Exception("not eligible")
