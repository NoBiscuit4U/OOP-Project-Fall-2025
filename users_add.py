import streamlit as st
import UserManager
from User import User

um=UserManager.UserManager()

with st.container(horizontal_alignment="center"):
    st.button("Access Users", key="users_access")

    if st.session_state.users_access:
        st.button("Add User", key="add_user")
        st.text_input("ID", key="user_input_id")
        st.text_input("Name", key="user_input_name")
        st.text_input("Password", key="user_input_password")
        st.text_input("Credentials", key="user_input_creds")
        st.text_input("Email", key="user_input_email")

        st.button("Submit", key="user_input_submit")

        if st.session_state.user_input_submit:
            user = User(
                st.session_state.user_input_id,
                st.session_state.user_input_name,
                st.session_state.user_input_password,
                st.session_state.user_input_creds,
                st.session_state.user_input_email,
            )