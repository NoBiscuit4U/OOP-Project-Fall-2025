import streamlit as st
import pandas as pd

with st.container(horizontal_alignment="center"):



    st.text_input("Search", key="book_search_input")
    st.selectbox("Search Criteria", options=["ID", "Author", "Title"], key="book_search")




    confusion_matrix = pd.DataFrame(
        st.session_state.bm.get_books_info(),
        columns=st.session_state.bm.get_keys()
        )
    st.dataframe(confusion_matrix, height="auto")