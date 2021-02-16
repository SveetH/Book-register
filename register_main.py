from register_db import create_table
from register_actions import add_user, get_stat, info_user, del_user

create_table()
commands = ('1', '2', '3', '4', '5')

print("------ Welcome to the Library! ------")
print("Options: \n1.Add user\n2.User library\n3.Registered users\n4.Delete user\n5.Exit\n")

command = input("Please choose option: ")
while command != "5":
    if command == "1":
        add_user()

    if command == "2":
        info_user()

    if command == "3":
        get_stat()

    if command == "4":
        del_user()

    if command not in commands:
        print('--> Wrong option, try again')
    else:
        print("Options: \n1.Add user\n2.User library\n3.Registered users\n4.Delete user\n5.Exit\n")
    command = input("Please choose option: ")

print("-------------")
print("--Good bye!--")
print("-------------")
