from users import user
class library:
    def __init__ (self):
        self.users=[]
        self.books=[]

    def add_users(self,user):
        self.users.append(user)

    def add_books(self,book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())

    def verify(self):
            name=input(f"Enter the username: ")
            i=1
            repeat=True
            while repeat:
                for i in self.users:
                    if name == i.name:
                        print(f"This username was already taken, please use a different one")
                        name=input(f"Enter the username: ")
                        break
                else:
                    return(name)
                
    def login(self,name):
        for i in self.users:
            if name==i.name:
                login=i.check_password(name)
                return(login)
        print("Username not found")

    def return_book(self,title):
        for i in self.books:
            if title==i.title:
                if i.available==False:
                    i.available=True
                    print("Book returned succesfully")
                    break
                else:
                    print("Book has not been borrowed")
                    break
        else:
            print ("Book not found")

