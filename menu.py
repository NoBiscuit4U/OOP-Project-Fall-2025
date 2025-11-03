#import user, editor, and book classes
import pickle

print("Welcome to the _____ library management system.")

list_of_options = ["display menu", "add book", "add user", "edit book", "edit user", "get book catalogue", "display users", "check out book", "return book", "quit"] #not all options

while True:
    user_choice = input("What would you like to do? ")

    if user_choice == "display menu":
        for option in list_of_options:
            print(option)

    elif user_choice == "2":
        break

    elif user_choice == "3":
        break

    elif user_choice == "4":
        break

    elif user_choice == "5":
        break

    elif user_choice == "6":
        break

    elif user_choice == "7":
        break

    elif user_choice == "8":
        break

    elif user_choice == "9":
        break










    elif user_choice == "quit":
        break

    else:
        print("Sorry, that is not a valid option. Please try again.")