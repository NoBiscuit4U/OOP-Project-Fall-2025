import streamlit as st
from requests import session
from streamlit import session_state

import UserManager

st.title("**Library Management System**")
if not st.session_state.login_success:
    with st.container(horizontal_alignment="center"):

        st.text_input("ID", key="login_id")
        st.text_input("Password", key="login_password")

        st.button("Login",key="login_submit")

        if st.session_state.login_submit:
            if st.session_state.um.check_cred(st.session_state.login_id,st.session_state.login_password):
                print("True")
                st.session_state.login_success = True
                st.rerun()
            else:
                st.session_state.login_success = False
