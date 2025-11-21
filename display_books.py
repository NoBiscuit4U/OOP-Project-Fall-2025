import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):
    @st.dialog("Book Edited")
    def user_edited():
        st.write("Book Edited")

    @st.dialog("Missing Information")
    def missing_info():
        st.write("Check that all fields are filled")

    @st.dialog("Duplicate ID")
    def dup_id():
        st.write("A book with this ID already exists")

    st.text_input("ID", key="which_book_input_id")
    st.text_input("Which value do yu want to edit? ", key="which_book_value_input")
    st.text_input("What do you want the new value to be? ", key="new_book_value_input")

    st.button("Submit", key="edit_book_input_submit")

    confusion_matrix = pd.DataFrame(
        st.session_state.bm.get_books_info(),
        columns=st.session_state.bm.get_keys()
    )
    st.table(confusion_matrix, border="horizontal")