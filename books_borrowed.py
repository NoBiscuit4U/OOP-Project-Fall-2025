import streamlit as st

if "shelf_login_success" not in st.session_state:
    st.session_state.shelf_login_success=False

@st.dialog("Books N/A")
def no_books():
    st.write("No Books on Account")

@st.dialog("Returned")
def returned_book():
    st.write(f"Returned {st.session_state.l_return_book}")

def return_book(book_id):
    st.session_state.um.return_book(st.session_state.books_borrowed_user_shelf_ID,book_id)
    st.session_state.l_return_book=book.get_info("title")
    returned_book()

st.title("**Shelf**")

st.text_input("User ID", key="books_borrowed_user_shelf_ID")
st.button("Search", key = "search_books_borrowed_user_shelf_id")
if st.session_state.search_books_borrowed_user_shelf_id and not st.session_state.books_borrowed_user_shelf_ID == "":
    usr=st.session_state.um.get_unique_user("id",st.session_state.books_borrowed_user_shelf_ID)
    books=usr.get_info("books")
    i=0

    if len(books)>0:
        for book in books:
            st.button(f"Return {book.get_info("title")}", key = f"return_borrowed_book{i}",on_click=return_book,kwargs={"book_id":book.get_info("id")})
            i+=1
    else:
        no_books()