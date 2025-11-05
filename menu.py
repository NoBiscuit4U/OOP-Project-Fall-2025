#import user, editor, and book classes
import pickle
import streamlit as st
from ReadWriter import ReadWriter
from Book import Book
from User import User

list_of_options = ["display menu", "add book", "add user", "edit book", "edit user", "get book catalogue", "display users", "check out book", "return book", "quit"] #not all options

rw = ReadWriter

while True:
    """Ask Daniel if we should have a log in to separate the patrons from the librarians"""
    user_choice = input("What would you like to do? ")

    if user_choice == "display menu":
        for option in list_of_options:
            print(option)

    elif user_choice == "add":
        add_choice = input("Do you want to add a book or a user? ")
        if add_choice == "book":
            book_id = input("What is the book's ID? ")
            title = input("What is the book's title? ")
            author = input("Who is the book's author? ")
            pub_date = input("When was the book published? mm/dd/yyyy ")
            price = input("What is the book's price? ")
            sku = input("SKU")
            book = Book(book_id,title,author,pub_date,price,sku)
            rw.append_file(book)

        elif add_choice == "user":
            user_id = input("What is the user's ID? ")
            name = input("What is the user's name? ")
            password = input("Who is the book's author? ")
            creds = input("When was the book published? mm/dd/yyyy ")
            email = input("What is the book's price? ")
            user = User(user_id,name,password,creds,email)
            rw.append_file(user)

    elif user_choice == "edit":
        edit_choice = input("Do you want to edit a book or a user? ")
        if edit_choice == "book":
            break

        elif edit_choice == "user":
            break

    elif user_choice == "display":
        display_choice = input("Do you want to display a user or a book? ")
        if display_choice == "user":
            book_choice = input("What book do you want to display? ")
            search_criteria = input("what do you want to search useing? (Author, ID, Title, Publication Date)")
            rw.get_unique_obj(search_criteria, book_choice)

    elif user_choice == "check out":
        break

    elif user_choice == "return":
        break

    elif user_choice == "quit":
        break

    else:
        print("Sorry, that is not a valid option. Please try again.")