from register_db import *
from time import time, ctime
from books import books
from books_db import create_book_table

t = time()
register = {}


def confirm():
    command = input("Are you sure [Y/N]: ")
    if command in ('Y', 'y'):
        return 1
    if command in ('N', 'n'):
        return 2
    else:
        print("Incorrect answer")
        return confirm()


def add_user():
    user_name = input("Please enter username: ")
    user_val = True
    while user_val:
        for entry in get_entries():
            if entry[0] == user_name:
                print(f"--{user_name} already registered, try other username--")
                user_name = input("Please enter username: ")
            else:
                user_val = False
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    while True:
        try:
            tel_number = int(input("Please enter your phone: "))
            add_user_to_db(user_name, first_name, last_name, tel_number, ctime(t))
            break
        except ValueError:
            print("-->Only numbers!")

    create_book_table(user_name)
    print(f"-->Username {user_name} has been successfully added\n")


def info_user():
    searched_user_name = input("Please enter username: ")
    find = False
    for entry in get_entries():
        if searched_user_name == entry[0]:
            print("---------------------------------------")
            print(f"Welcome to {searched_user_name}'s library")
            print("---------------------------------------")
            print(
                f"--- Info about {entry[0]} ---\n--- First name : {entry[1]}\n--- Last name : {entry[2]}\n"
                f"--- Phone : {entry[3]}\n")
            print("------------------------")

            books(searched_user_name)
            find = True
            break
    if not find:
        print("-->There is no such username in the register\n")


def get_stat():
    entries = get_entries()
    if len(entries) > 0:
        print("---Statistics---\n")
        statistics = ""
        n = 1
        for el in entries:
            statistics += f"{n}.{el[0]} -- {el[1]} {el[2]}, phone: {el[3]}, registered: {el[4]}\n"
            n += 1
        print(statistics)
        print("----------------------------")
        print(f"Total persons: {len(entries)}")
        print("----------------------------")
    else:
        print("----- No data -----")


def del_user():
    user_name = input("Please enter username who wants to be deleted: ")
    validation = True
    for entry in get_entries():
        if entry[0] == user_name:
            confirmed = confirm()
            if confirmed == 1:
                del_user_from_db(user_name)
                print(f"--- Username {user_name} has been deleted! ---")
                validation = False
                break
            if confirmed == 2:
                validation = False
                break
    if validation:
        print("No user with that username!")
