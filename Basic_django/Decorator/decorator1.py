#decorator function - without changing code add extra feature to not repeat a function
#DRY - donot repeat yourself


#program to always get higher-lower value

def dec_fun(fn): #decorator function need a function inside
    def inner_fun(n1,n2): #dectorator function always have inner function
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)  #function has arguements in sub/div
    return inner_fun  #call inner function inside decorator function

@dec_fun
def sub(n1,n2):
    return n1-n2

@dec_fun
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(sub(20,10))
print(div(10,20))
