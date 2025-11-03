import streamlit as st

st.title("**Library Management System**")
with st.container(horizontal=True, horizontal_alignment="center"):

    st.text_input("Username",key="username")
    st.text_input("Password",key="password")