from operator import truediv

import streamlit as st
import UserManager
from User import User

@st.dialog("Missing Information")
def missing_info():
    st.write("Check that the ID, Name, and Password are not blank")

@st.dialog("Duplicate ID")
def dup_id():
    st.write("A user with this ID already exists")

@st.dialog("User Created")
def user_created():
    st.write("User Created")

with st.container(horizontal_alignment="center"):
    st.text_input("ID", key="user_input_id")
    st.text_input("Name", key="user_input_name")
    st.text_input("Password", key="user_input_password")
    st.selectbox("Credentials",options=["none","admin"],key="user_input_creds")
    st.text_input("Email", key="user_input_email")

    st.button("Submit", key="user_input_submit")

    if st.session_state.user_input_submit:
        if not st.session_state.user_input_id=="" and not st.session_state.user_input_name=="" and not st.session_state.user_input_password=="":
            id_check=True

            for obj in st.session_state.um.get_users():
                if obj.get_info("id")==st.session_state.user_input_id:
                    id_check=False

            if id_check:
                st.session_state.um.new_user_write(
                    st.session_state.user_input_id,
                    st.session_state.user_input_name,
                    st.session_state.user_input_password,
                    st.session_state.user_input_creds,
                    st.session_state.user_input_email,
                )
                user_created()
            else:
                dup_id()
        else:
            missing_info()

