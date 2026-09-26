from books import book
from users import user
from library import library

#Creating instances
book1=book(1,"OOP Fundamentals", "Jhon L", "BBC")
book2=book(2,"Phyton for dummies", "Stef Maruzh", "For dummies")

user1=user(1,"Leonardo Ramirez", "1234")

library1=library()

#Creating associations
library1.add_books(book1)
library1.add_books(book2)
library1.add_users(user1)

library1.show_books()
library1.show_users()

#Variable to control the cycle
option=0

#set at 1 and 2 because of the instances created previously
user_id=1
book_id=2

#Menu to choose wheter to register an user/book or borrowing/return a book 
while option!=5:
    option=int(input(f"What will you do?: "))
    match option:
        case 1:
            name=library1.verify()
            password=input(f"Enter the password: ")
            user1=user(user_id+1,name,password)
            user_id+=1
            library1.add_users(user1)
        case 2:
            title=input(f"Enter the title of the book: ")
            author=input(f"Enter the author of the book: ")
            editorial=input(f"Enter the editorial of the book")
            book1=user(book_id+1,title,author,editorial)
            book_id+=1
            library1.add_books(book1)
        case 3:
            name=input(f"Enter your username: ")
            login=library1.login(name)
            if login:
                borrow_book=input("Enter the title of the book you want to borrow")
                for i in library1.books:
                    if borrow_book == i.title:
                        if i.available==True:
                            i.available=False
                            for u in library1.users:
                                if name==u.name:
                                    u.borrow_book(borrow_book)
                                    print("Operation succesful")
                                    break
                        else:
                            print ("The book has already been borrowed")
                            break
                else:
                    print(f"Book not found")
        case 4:
            name=input(f"Enter your username: ")
            login=library1.login(name)
            if login:
                title=input(f"Enter the title of the book")
                for u in library1.users:
                    if name == u.name:
                        if title in u.borrowed_books:
                            library1.return_book(title)
                            u.return_book(title)
                            break
                    else:
                        print(f"This user didnt borrow the book")
                        break

#Requirements
#1.- The system must allow registering books
#2.- The system must allow register users
#3.- The system must allow a book to be borrowed by a user
#4.- A book that has already been borrowed cannot be borrowed again
#5.- The system must allow a book to be returned