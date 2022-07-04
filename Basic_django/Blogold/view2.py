from Blog.model1 import users,posts

def authenticate(**kwargs):  #use kwargs for dict format
    #username=kwargs[username]
    username=kwargs.get("username")  #use get function to avoid server error
    email=kwargs.get("email")
    user_data=[i for i in users if i["username"]==username and i["email"]==email]
    return user_data

#get - to retrieve
#post - to submit

session={}  #if login success, store username in a dictionary to not ask login again

#use decorator to check whether logged in for all class
def loginrequired(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper

class SignInview:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("login success")
            session["user"]=username
        else:
            print("invalid credentials")

@loginrequired
def logout(*args,**kwargs):
    session.pop("user")

class PostListview:
    @loginrequired
    def get(self,*args,**kwargs):
        return posts

signin=SignInview()
signin.post(username="Bret",email="Sincere@april.biz")
print(session)

postlist=PostListview()
allpost=postlist.get()
for p in allpost:
    print(p)

logout()
print(session)



