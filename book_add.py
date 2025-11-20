import streamlit as st
import BookManager
from Book import Book

bm = BookManager()

@st.dialog("Missing Information")
def missing_info():
    st.write("Check that the ID, Title, Author, Publication Date, Price, and SKU are not blank")

@st.dialog("Duplicate ID")
def dup_id():
    st.write("A book with this ID already exists")

with st.container(horizontal_alignment="center"):
    st.text_input("ID", key="book_input_id")
    st.text_input("Title", key="book_input_title")
    st.text_input("Author", key="book_input_author")
    st.selectbox("Publication Date",key="book_input_pub_date")
    st.text_input("Price", key="book_input_price")
    st.text_input("SKU", key="book_input_sku")

    st.button("Submit", key="book_input_submit")

    if st.session_state.book_input_submit:
        if not st.session_state.book_input_id=="" and not st.session_state.book_input_title=="" and not st.session_state.book_input_author=="":
            print(st.session_state.bm.get_unique_book("id",st.session_state.book_input_id))
            if st.session_state.bm.get_unique_book("id",st.session_state.book_input_id)==None:
                st.session_state.bm.new_user_write(
                    st.session_state.book_input_id,
                    st.session_state.book_input_title,
                    st.session_state.book_input_author,
                    st.session_state.book_input_pub_date,
                    st.session_state.book_input_price,
                    st.session_state.book_input_sku,

                )
            else:
                dup_id()
        else:
            missing_info()