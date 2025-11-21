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

    st.text_input("ID", key="which_user_input_id")
    st.text_input("Which value do yu want to edit? ", key="which_user_value_input")
    st.text_input("What do you want the new value to be? ", key="new_user_value_input")

    st.button("Submit", key="edit_user_input_submit")

    confusion_matrix = pd.DataFrame(
        st.session_state.um.get_users_info(),
        columns=st.session_state.um.get_keys()
    )

    st.table(confusion_matrix, border="horizontal")



