import streamlit as st
from requests import session
from streamlit import session_state

import UserManager

st.session_state.um=UserManager.UserManager()

def logout():
    if st.button("Log out"):
        st.session_state.login_success=False
        st.rerun()

login=st.Page("login.py",title="Login")

logout=st.Page(logout,title="Logout")

user_add=st.Page("users_add.py",title="Add User")

if "login_success" not in st.session_state:
    st.session_state.login_success=False

if not st.session_state.login_success:
    pg=st.navigation([login])
else:
    pg=st.navigation({
        "Account":[logout],
        "User Management":[user_add],
        "Book Management":[],
        "Checkout":[]
    })

pg.run()