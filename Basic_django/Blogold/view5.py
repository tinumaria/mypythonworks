from Blog.model1 import users,posts

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user1 for user1 in users if user1["username"]==username and user1["email"]==email]
    return user_data

session={}

class Signin:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user2=authenticate(username=username,email=email)
        if user2:
            print("logged in")
            session["user3"]=username
        else:
            print("invalid credentials")

def Login(fn):
    def innerlogin(*args,**kwargs):
        if "user3" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return innerlogin

class Allpost:
    @Login
    def get(self,*args,**kwargs):
        return posts

class Mypost:
    @Login
    def get(self,*args,**kwargs):
        loguser=session.get("user")
        user_id=[user4["id"] for user4 in users if user4["username"]==loguser][0]
        post_details=[post for post in posts if post["userId"]==user_id]
        print(post_details)

def logout(*args,**kwargs):
    session.pop("user3")

sign=Signin()
sign.post(username="Antonette",email="Shanna@melissa.tv")

print(session)

all=Allpost()
allpost=all.get()
for i in allpost:
    print(i)

my=Mypost()
my.get()

logout()
print(session)

