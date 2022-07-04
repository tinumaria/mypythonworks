from Blog.model1 import users  #syntax: from package.module import items

def authenticate(username,email):
    user_data=[i for i in users if i["username"]==username and i["email"]==email]
    return user_data
user=authenticate("Bret","Sincere@april.biz") #authenticate is to look given value correct or not
if user:
    print("login success")
else:
    print("invalid")

#but we need in dictionary format by using kwargs
#refer next file


