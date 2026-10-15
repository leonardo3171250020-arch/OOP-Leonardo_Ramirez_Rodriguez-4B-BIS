class user:
    def __init__(self, id_user, name, password):
        self.id_user=id_user
        self.name=name
        self.__password=password
        self.borrowed_books=[]

    def show_user_info(self):
        return f"{self.id_user} - {self.name}"

    def check_password(self,username):
        login=False
        user=self.name
        __password=self.__password
        while not login:
            password=input("Password: ")
            if user==username and __password==password:
                login=True
        return(login)

    def borrow_book(self,title):
        self.borrowed_books.append(title)

    def return_book(self,title):
        self.borrowed_books.remove(title)