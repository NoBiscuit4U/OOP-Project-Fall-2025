import streamlit as st
import UserManager

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
        st.button("Access Users")
        st.button("Access Books")