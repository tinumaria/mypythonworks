#sum using *args

def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(3,4,10))
