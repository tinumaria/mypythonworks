#remove special characters from sample file

f=open("sample", "r")
specl='!@#$%^&*()'

for i in f:
    data=i.rstrip("\n")
    print(data)
    strng=''
    for j in data:
        if j not in specl:
            strng+=j
print(strng)


