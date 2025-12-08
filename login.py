import streamlit as st

st.title("**Library Management System**")
if not st.session_state.login_success:
    with st.container(horizontal_alignment="center"):

        st.text_input("Username", key="login_name")
        st.text_input("Password", key="login_password")

        st.button("Login",key="login_submit")

        if st.session_state.login_submit:
            if st.session_state.um.check_cred(st.session_state.login_name,st.session_state.login_password):
                print("True")
                st.session_state.login_success = True
                st.rerun()
            else:
                st.session_state.login_success = False
