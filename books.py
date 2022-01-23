from books_db import add_new_book, view_all_books, view_read_books, read_a_book
# modified

# added new func
def new_func(name):
    print(name)

def new_book(user):
    title = input("Enter book's title: ")
    add_new_book(title, user)
    print("------------------------------------------------")
    print(f"{title} book was added to {user}'s library!")
    print("------------------------------------------------")


def all_books(user):
    book_list = view_all_books(user)
    if len(book_list) > 0:
        print(f"--- {user}'s all books ---")
        print("--------------------------------")
        for entry in book_list:
            if entry[1] == 0:
                status = "Not read"
            else:
                status = "Read"
            print(f"-- {entry[0]} -- status: {status}")
        print("--------------------------------")
    else:
        print("---- No books in the library ----")


def read_books(user):
    book_list = view_read_books(user)
    if len(book_list) > 0:
        print(f"--- books that {user} has been read ---")
        print(f"---------------------------------------")
        for entry in book_list:
            print(f"-- {entry[0]} -- ")
        print(f"---------------------------------------")
    else:
        print("---- No read books in the library ----")


def read(user):
    title = input("Which book would like to read: ")
    book_list = view_all_books(user)
    is_read = True
    for book in book_list:
        if book[0] == title:
            if book[1] == 0:
                read_a_book(user, title)
                print(f"-----------------------------------------------------------------------")
                print(f"-- Congrats!You finnish the book {title} , it was exciting journey! --")
                print(f"-----------------------------------------------------------------------")
                is_read = False
            else:
                print(f"------------------------------------------------------")
                print("-- You've already read that one.Go ahead, and read it again! -- ")
                print(f"------------------------------------------------------")
                is_read = False
    if is_read:
        print(f"-------------------------------------------")
        print("-- No book with that name in the library --")
        print(f"-------------------------------------------")


def books(user):
    commands = ('1', '2', '3', '4', '5')
    print("Options: \n1.Add new book\n2.View all books\n3.View read books\n4.Read a book\n5.Exit\n")

    command = input("Please choose option: ")
    while command != "5":
        if command == "1":
            new_book(user)

        if command == "2":
            all_books(user)

        if command == "3":
            read_books(user)

        if command == "4":
            read(user)

        if command not in commands:
            print('--> Wrong option, try again')
        else:
            print("Options: \n1.Add new book\n2.View all books\n3.View read books\n4.Read a book\n5.Exit\n")
        command = input("Please choose option: ")
