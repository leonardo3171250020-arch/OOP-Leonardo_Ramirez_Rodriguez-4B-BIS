#First Class: User
class User:
    #Attributes
    def __init__(self,name,__password,followers):
        self.name=name
        self.__password=__password
        self.followers=followers 

    #Methods
    def login(self,name,__password):
        login=False
        user=self.name
        __password=self.__password
        while not login:
            username=input("username: ")
            password=input("Password: ")
            if user==username and __password==password:
                login=True

    def Checkfollowers(self,followers):
        print(f"You have {self.followers} followers")

    def create_post(self,content,title):
        return Post(title,content,self.name,0)

    def comentar(self,content,post):
        return Comments(self.name,content,post.title)

    def send_message(self,message,receiver):
        return Messages(self.name,message,receiver)
    
#Second Class: Posts
class Post:
    #Attributes
    def __init__(self,content,title,author,likes):
        self.content=content
        self.title=title
        self.likes=likes
        self.author=author

    #Methods
    def Checkinfo(self):
        print(f"{self.title}\n{self.content}\n{self.likes} likes\to {self.author}")

    def like(self,likes):
        self.likes+=1
        return(self.likes)

#Third Class: Comments
class Comments:
    #Attributes
    def __init__(self,text,author,receiver):
        self.text=text
        self.author=author
        self.receiver=receiver

    #Methods
    def CheckComment(self):
        print(f"{self.author} commented {self.text} in {self.receiver}")

    def like(self):
        self.likes+=1
        return(self.likes)

#Fourth Class: Messages/DMs
class Messages:
    #Attributes
    def __init__(self,name,message,receiver):
        self.name=name
        self.message=message
        self.receiver=receiver

    #Methods
    def CheckMessage(self):
        print(f"Message was sent by {self.name}\n {self.message}\n sent to {self.receiver}")

    def ChangeName(self):
        self.name=input("Name: ")
        return (self.name)

user1=User("leo",1234,100)
user2=User("juan",4215,120)
post1=user1.create_post("Hi everyone!","Im an IT engineer")
post1.Checkinfo()
comment1=user2.comentar("Hi!!!!!!!!", post1)
comment1.CheckComment()
message1=user1.send_message("Hello, this is a message", user2.name)
message1.CheckMessage()
