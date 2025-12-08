import streamlit as st
import pandas as pd

st.title("**Shelf**")



with st.container(horizontal_alignment="center"):
    @st.dialog("Missing Information")
    def missing_info():
        st.write("Check that all fields are filled")


    @st.dialog("Book Returned")
    def book_returned():
        st.write("Book Returned")

    st.text_input("ID", key="return_user_id_input")

    st.button("Submit", key="return_user_submit")

    usr_id = st.session_state.return_user_id_input

    user = st.session_state.um.get_unique_user("ID", usr_id)

    if st.session_state.return_user_submit:
        if not st.session_state.return_user_id_input == "":
            book_returned()
        else:
            missing_info()

    confusion_matrix = pd.DataFrame(
            st.session_state.bm.get_books_info(),
            columns=st.session_state.bm.get_keys()
        )
    st.dataframe(confusion_matrix, height="auto")





