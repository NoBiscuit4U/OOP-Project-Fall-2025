import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):
    @st.dialog("Book Edited")
    def book_edited():
        st.write("Book Edited")

    @st.dialog("Missing Information")
    def missing_info():
        st.write("Check that all fields are filled")
    
    @st.dialog("Book Removed")
    def book_removed():
        st.write("Removed Unique")

    st.text_input("ID", key="book_uid_input")
    st.selectbox("Operation To Perform",options=["Edit","Remove"],key="book_operations")
    
    if st.session_state.book_operations=="Edit":
        st.text_input("Column Value to Edit?", key="book_key_input")
        st.text_input("New Value?", key="book_nvalue_input")
        st.button("Submit", key="edit_book_submit")

        if st.session_state.edit_book_submit:
            if not st.session_state.book_uid_input =="" and not st.session_state.book_key_input == "" and not st.session_state.book_nvalue_input == "":
                st.session_state.bm.edit_unique_book(st.session_state.book_uid_input,st.session_state.book_key_input, st.session_state.book_nvalue_input)
                book_edited()
            else:
                missing_info()

    elif st.session_state.book_operations=="Remove":
        st.button("Remove", key="remove_book_submit")

        if st.session_state.remove_book_submit:
            if not st.session_state.book_uid_input =="":
                st.session_state.bm.remove_unique_book(st.session_state.book_uid_input)
                book_removed()
            else:
                missing_info()


    confusion_matrix = pd.DataFrame(
        st.session_state.bm.get_books_info(),
        columns=st.session_state.bm.get_keys()
    )
    st.dataframe(confusion_matrix,height="auto")