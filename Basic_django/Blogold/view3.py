from Blog.model1 import users,posts

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[i for i in users if i["username"]==username and i["email"]==email]
    return user_data

session={}

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

class MyPostview:
    @loginrequired
    def get(self,*args,**kwargs):
        loggeduser=session.get("user")
        userId=[user["id"] for user in users if user["username"]==loggeduser][0]
        mypos=[post for post in posts if post["userId"]==userId]
        print(mypos)

signin=SignInview()
signin.post(username="Bret",email="Sincere@april.biz")

mypost=MyPostview()
mypost.get()


