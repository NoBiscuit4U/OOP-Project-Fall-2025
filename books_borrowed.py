import streamlit as st

if "shelf_login_success" not in st.session_state:
    st.session_state.shelf_login_success=False

st.title("**Shelf**")




st.text_input("User ID", key="books_borrowed_user_shelf_ID")
st.button("Search", key = "search_books_borrowed_user_shelf_id")
if st.session_state.search_books_borrowed_user_shelf_id and not st.session_state.books_borrowed_user_shelf_ID == "":
    usr_shelves = st.session_state.um.get_users()
    for usr in usr_shelves:
        if usr.i_id == st.session_state.books_borrowed_user_shelf_ID:
            for book in usr.books_borrowed:
                st.text(book)
                st.button("Return", key = "return_borrowed_book")
                if st.session_state.return_borrowed_book:
                    st.text("Returned: ", book)
                    st.session_state.usr.return_book()










