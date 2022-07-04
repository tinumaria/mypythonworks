from Basic_django.Blognew.models import users,posts

#1. Authenticate

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user_data=[user for user in users if user["username"]==username and user["password"]==password]
    return user_data

# print(authenticate(username="anu",password="Password@123"))

#get - retrieve
#post - submit/create
#put/patch - edit/update
#delete - remove

session={}

#7. decorator

def signinrequired(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper

#2. Signin

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user_details=authenticate(username=username,password=password) #call authenticate here instead of in method authenticate above
        if user_details:
            session["user"]=user_details[0]
            print("login success")
        else:
            print("invalid")

signin=SignInView()
signin.post(username="richard",password="Password@123")

print(session)

#3. List all post & create a post

class PostsView:
    #listallpost
    @signinrequired
    def get(self,*args,**kwargs):
        return posts

    #cretepost
    @signinrequired
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        print(kwargs)
        posts.append(kwargs)
        print(posts)


data=PostsView()
print(data.get())

data.post(postId=9,
      title="haidaa",
      content="finedaa",
      likedby=[])

#4. list users post

class MyPostView:
    @signinrequired
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        print(userId)
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post

mypost=MyPostView()
print(mypost.get())

#5. delete & update post

# class PostdetailView:w
#     def delete(self,*args,**kwargs):
#         post_id=kwargs.get("post_id")
#         post_data=[post for post in posts if post["postId"]==post_id]
#         if post_data:
#             post_delete=post_data[0]  #to remove list
#             posts.remove(post_delete)
#             print("post removed")
#             print(len(posts))

class PostdetailView:
    def get_object(self,id):
        post_details=[post for post in posts if post["postId"]==id]
        return post_details

    @signinrequired
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post_details=self.get_object(post_id)
        return post_details

    @signinrequired
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post_data=self.get_object(post_id)
        if post_data:
            post_delete=post_data[0]  #to remove list
            posts.remove(post_delete)
            print("post removed")
            print(len(posts))

    @signinrequired
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        post_data=self.get_object(post_id)
        if post_data:
            post_update=post_data[0]
            post_update.update(data)
            return post_update


postddetail=PostdetailView()

postddetail.delete(post_id=6)
print(postddetail.get(post_id=3))

data={
    "title":"new title",
    "content":"new content"
}

print(postddetail.put(post_id=4,data=data))

#6. like

class LikeView:
    @signinrequired
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post_like=[post for post in posts if post["postId"]==postid]
        if post_like:
            postlike=post_like[0]
            userid=session["user"]["id"]
            postlike["liked_by"].append(userid)
            print(postlike)

like=LikeView()
like.get(postid=3)

#8. logout

def signout(*args,**kwargs):
    session.pop("user")
    print(user["username"],"has logged out")

signout()
