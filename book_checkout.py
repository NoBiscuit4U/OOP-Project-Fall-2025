import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):


    st.text_input("Search", key="book_search_input")
    st.selectbox("Search Criteria", options=["ID", "Author", "Title"], key="book_search")

    st.button("Search", key="return_book_search")

    if st.session_state.return_book_search:
        if st.session_state.book_search == ID:
            for book in pd.DataFrame():
                #if the book's ID is equal to a book ID, show the book
                # if not say this book is not in the library.