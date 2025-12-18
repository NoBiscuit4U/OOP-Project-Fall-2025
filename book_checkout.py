import streamlit as st
import pandas as pd
import TokenSearch as ts

@st.dialog("Search Returned Nothing")
def na_search():
    st.write(f"Nothing Under Search Term, Try Different Criteria")

@st.dialog("ID N/A")
def na_id():
    st.write(f"Ensure Fields for ID are Populated")

@st.dialog("Checkout Complete")
def checkout_fin():
    st.write(f"Book: {st.session_state.l_book_check}")
    st.write(f"Checked out to User: {st.session_state.l_user_check}")

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
        else:
            na_search()
    
    st.text_input("User ID", key="checkout_user_id")
    st.text_input("Book ID", key="checkout_book_id")
    st.button("Add to Account",key="checkout_add_account")

    if st.session_state.checkout_add_account and not st.session_state.checkout_book_id=="" and not st.session_state.checkout_book_id=="":
        st.session_state.um.borrow_book(st.session_state.checkout_user_id,st.session_state.bm.get_unique_book("id",st.session_state.checkout_book_id))
        st.session_state.l_book_check=st.session_state.bm.get_unique_book("id",st.session_state.checkout_book_id).get_info("title")
        st.session_state.l_user_check=st.session_state.um.get_unique_user("id",st.session_state.checkout_user_id).get_info("name")
        checkout_fin()
    elif not st.session_state.book_search_submit and st.session_state.checkout_add_account:
        na_id()