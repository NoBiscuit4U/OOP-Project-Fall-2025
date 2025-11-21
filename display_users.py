from operator import index

import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):
    @st.dialog("User Edited")
    def user_edited():
        st.write("User Edited")

    @st.dialog("Missing Information")
    def missing_info():
        st.write("Check that the ID, Name, and Password are not blank")

    @st.dialog("Duplicate ID")
    def dup_id():
        st.write("A user with this ID already exists")

    st.text_input("ID", key="user_uid_input")
    st.text_input("Which value do yu want to edit? ", key="user_key_input")
    st.text_input("What do you want the new value to be? ", key="user_nvalue_input")

    st.button("Submit", key="edit_user_submit")

    if st.session_state.edit_user_submit:
        if not st.session_state.user_uid_input =="" and not st.session_state.user_key_input == "" and not st.session_state.user_nvalue_input == "":
            st.session_state.um.get_unique_user("ID", st.session_state.user_uid_input).edit_info(st.session_state.user_key_input, st.session_state.user_nvalue_input)
            st.rerun()
            user_edited()

        else:
            missing_info()

    confusion_matrix = pd.DataFrame(
        st.session_state.um.get_users_info(),
        columns=st.session_state.um.get_keys()
    )

    st.dataframe(confusion_matrix,height="auto")



