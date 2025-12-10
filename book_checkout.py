import streamlit as st
import pandas as pd
import TokenSearch as ts

tks=ts.TokenSearch(st.session_state.bm)

with st.container(horizontal_alignment="center"):

    st.text_input("Search", key="book_search_input")
    st.selectbox("Search Criteria", options=["ID", "Author", "Title"], key="book_criteria")

    if "data_s" not in st.session_state:
        st.session_state.data_s = confusion_matrix = pd.DataFrame(
                                    st.session_state.bm.get_books_info(),
                                    columns=st.session_state.bm.get_keys()
                                )

    st.button("Submit",key="book_search_submit")

    st.dataframe(data=st.session_state.data_s,height="auto",key="book_df")

    if st.session_state.book_search_submit:
        return_books=tks.token_search(st.session_state.book_search_input,st.session_state.book_criteria,seperator=" ")

        if len(return_books)!=0:
            st.session_state.data_s = pd.DataFrame(
                                        return_books,
                                        columns=st.session_state.bm.get_keys()
                                    )

            st.rerun()