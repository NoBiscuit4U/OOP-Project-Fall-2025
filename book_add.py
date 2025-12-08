import streamlit as st
import random as rand

@st.dialog("Missing Information")
def missing_info():
    st.write("Check that the Title, and Author are not blank")

@st.dialog("Book Created")
def book_created():
    st.write("Book Created")

with st.container(horizontal_alignment="center"):
    st.text_input("Title", key="book_input_title")
    st.text_input("Author", key="book_input_author")
    st.text_input("Publication Date",key="book_input_pub_date")

    st.button("Submit", key="book_input_submit")

    if st.session_state.book_input_submit:
        if not st.session_state.book_input_title=="" and not st.session_state.book_input_author=="":
            n_id_base=""
            n_id=""
            p_str=st.session_state.book_input_title

            if not " " in p_str:
                tokens = [p_str[0]]
            else:
                tokens = p_str.split(" ")

            for token in tokens:
                n_id += token[0].upper()

            n_id += ("-"+str(rand.randint(0, 1000)))

            for obj in st.session_state.um.get_users():
                if obj.get_info("id") == n_id:
                    n_id=(n_id_base+"-"+str(rand.randint(0, 1000)))

            st.session_state.bm.new_book_write(
                n_id,
                st.session_state.book_input_title,
                st.session_state.book_input_author,
                st.session_state.book_input_pub_date
            )
            book_created()

        else:
            missing_info()
