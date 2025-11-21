import streamlit as st
from requests import session
from streamlit import session_state

import UserManager as uman
import BookManager as bman

st.session_state.um=uman.UserManager()
st.session_state.bm=bman.BookManager()

def logout():
    with st.container(horizontal_alignment="center"):
        if st.button("Log out"):
            st.session_state.login_success=False
            st.rerun()

login=st.Page("login.py",title="Login")

logout=st.Page(logout,title="Logout")

user_add=st.Page("users_add.py",title="Add User")

book_add=st.Page("book_add.py",title="Add Book")

book_bulk_add=st.Page("book_bulk_add.py",title="Bulk Book Creation")

if "login_success" not in st.session_state:
    st.session_state.login_success=False

if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded=False

if "bulk_edit_csv" not in st.session_state:
    st.session_state.bulk_edit_csv=""

if not st.session_state.login_success:
    pg=st.navigation([login])
else:
    pg=st.navigation({
        "Account":[logout],
        "User Management":[user_add],
        "Book Management":[book_add,book_bulk_add],
        "Checkout":[]
    })

pg.run()