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

def loggeduser():
    loggeduser=session.get("user")
    userId=[user["id"] for user in users if user["username"]==loggeduser][0]
    return userId

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
        user_id=loggeduser()
        mypos=[post for post in posts if post["userId"]==user_id]
        print(mypos)

class Createpost:
    @loginrequired
    def post(self,*args,**kwargs):
        userId=loggeduser()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userId,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")

class Specificpost():
    @loginrequired

    #read specific post
    def get(self,*args,**kwargs):
        id=kwargs.get("id")
        specpos=[spec for spec in posts if spec.get("id")==id]  #provide get to take from dic without error
        return specpos

    #update specific post - put
    def put(self,id=None,*args,**kwargs):
        post=[p for p in posts if p.get("id")==id][0]  #userid 1 le 6th id edkan ahnu 0th indexv
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)


signin=SignInview()
signin.post(username="Bret",email="Sincere@april.biz")

pst=Createpost()
pst.post(title="django",body="my post is django")

mypost=MyPostview()
mypost.get()

specpost=Specificpost()
print(specpost.get(id=5))

specpost.put(id=6,title="new post",body="this is my new post")