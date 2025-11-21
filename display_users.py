from operator import index

import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):
    @st.dialog("User Edited")
    def user_edited():
        st.write("User Edited")

    @st.dialog("Missing Information")
    def missing_info():
        st.write("Check that all fields are filled")

    @st.dialog("User Removed")
    def user_removed():
        st.write("Removed Unique")


    st.text_input("ID", key="user_uid_input")
    st.selectbox("Operation To Perform",options=["Edit","Remove"],key="user_operations")

    if st.session_state.user_operations=="Edit":
        st.text_input("Column Value to Edit?", key="user_key_input")
        st.text_input("New Value?", key="user_nvalue_input")

        st.button("Submit", key="edit_user_submit")
        if st.session_state.edit_user_submit:
            if not st.session_state.user_uid_input=="" and not st.session_state.user_key_input=="" and not st.session_state.user_nvalue_input=="":
                st.session_state.um.edit_unique_user(st.session_state.user_uid_input,st.session_state.user_key_input,st.session_state.user_nvalue_input)
                user_edited()
            else:
                missing_info()
    elif st.session_state.user_operations=="Remove":
        st.button("Remove", key="remove_user_submit")

        if st.session_state.remove_user_submit:
            if not st.session_state.user_uid_input =="":
                st.session_state.um.remove_unique_user(st.session_state.user_uid_input)
                user_removed()
            else:
                missing_info()

    confusion_matrix = pd.DataFrame(
        st.session_state.um.get_users_info(),
        columns=st.session_state.um.get_keys()
    )

    st.dataframe(confusion_matrix,height="auto")



