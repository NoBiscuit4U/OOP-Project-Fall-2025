import streamlit as st

if "shelf_login_success" not in st.session_state:
    st.session_state.shelf_login_success=False

st.title("**Shelf**")
if not st.session_state.shelf_login_success:
    with st.container(horizontal_alignment="center"):

        st.text_input("Username", key="which_user_name")
        st.text_input("Password", key="which_user_password")

        st.button("Login",key="shelf_login_submit")

        if st.session_state.shelf_login_submit:
            if st.session_state.um.check_cred(st.session_state.which_user_name,st.session_state.which_user_password):
                st.session_state.shelf_login_success = True
                st.rerun()
            else:
                st.session_state.shelf_login_success = False


if st.session_state.shelf_login_success==True:
    st.text("Hahahahahahahahahahahahahhahahahhahahahahahahhahahhahahahahahhahahahhaaha")









