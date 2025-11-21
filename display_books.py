import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):
    @st.dialog("Book Edited")
    def book_edited():
        st.write("Book Edited")

    @st.dialog("Missing Information")
    def missing_info():
        st.write("Check that all fields are filled")

    @st.dialog("Duplicate ID")
    def dup_id():
        st.write("A book with this ID already exists")

    st.text_input("ID", key="book_uid_input")
    st.text_input("Which value do yu want to edit? ", key="book_key_input")
    st.text_input("What do you want the new value to be? ", key="book_nvalue_input")

    st.button("Submit", key="edit_book_submit")

    if st.session_state.edit_book_submit:
        if not st.session_state.book_uid_input =="" and not st.session_state.book_key_input == "" and not st.session_state.book_nvalue_input == "":
            st.session_state.bm.get_unique_book("ID", st.session_state.book_uid_input).edit_info(st.session_state.book_key_input, st.session_state.book_nvalue_input)
            st.rerun()
            book_edited()

        else:
            missing_info()

    confusion_matrix = pd.DataFrame(
        st.session_state.bm.get_books_info(),
        columns=st.session_state.bm.get_keys()
    )
    st.dataframe(confusion_matrix,height="auto")