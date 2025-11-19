import streamlit as st
import UserManager
from User import User

um=UserManager.UserManager()

if "login_success" not in st.session_state:
    st.session_state.login_success=False

st.title("**Library Management System**")
if not st.session_state.login_success:
    with st.container(horizontal_alignment="center"):

        st.text_input("ID", key="id")
        st.text_input("Password", key="password")

        st.button("Login",key="login_submit")

        if st.session_state.login_submit:
            if um.check_cred(st.session_state.id,st.session_state.password):
                print("True")
                st.session_state.login_success = True
                st.rerun()
            else:
                st.session_state.login_success = False

else:
    with st.container(horizontal_alignment="center"):
        st.button("Access Users", key="users_access")
        st.button("Access Books", key="books_access")


        if st.session_state.users_access:
            st.button("Add User", key="add_user")
            st.text_input("ID", key="user_input_id")
            st.text_input("Name", key="user_input_name")
            st.text_input("Password", key="user_input_password")
            st.text_input("Credentials", key="user_input_creds")
            st.text_input("Email", key="user_input_email")
            user = User(st.session_state.add_user)


