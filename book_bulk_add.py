import streamlit as st
import pandas as pd
import numpy as np
import random as rand

@st.dialog("Error")
def file_error():
    st.write("Ensure File is uploaded")

with st.container(horizontal_alignment="center"):
    if not st.session_state.file_uploaded:
        with st.container(horizontal="center",key="fp_upload_contain",vertical_alignment="center"):
            st.file_uploader("File Upload .csv",key="csv_fp_upload",type="csv")

            st.button("Submit File",key="submit_csv")

            if st.session_state.submit_csv:
                if not st.session_state.csv_fp_upload==None:
                    st.session_state.bulk_edit_csv=pd.read_csv(st.session_state.csv_fp_upload,encoding="UTF-8")
                    st.session_state.file_uploaded=True
                    st.rerun()
                else:
                    file_error()
    else:
        st.button("Upload New .csv",key="upload_new_csv")

        if st.session_state.upload_new_csv:
            st.session_state.file_uploaded=False
            st.rerun()
        
        columns=st.session_state.bulk_edit_csv.columns
        options=np.append(["None"],columns)
        st.write("Choose Matching Columns")
        for key in st.session_state.bm.get_keys():
                if key=="ID":
                    id_options=np.append(["Generate IDs"],columns)
                    st.selectbox(f"Key: {key}",options=id_options,key=f"book_bulk_{key}")
                else:
                    st.selectbox(f"Key: {key}",options=options,key=f"book_bulk_{key}")

        st.button("Add Books",key="add_books_bulk")
        
        if st.session_state.add_books_bulk:
            n_id=0
            for i in range(0,st.session_state.bulk_edit_csv.size-1):
                print(st.session_state.bulk_edit_csv[st.session_state.book_bulk_Title][i])

                if st.session_state.book_bulk_ID=="Generate IDs":
                    n_id=rand.randint(0,999999)
                else:
                    n_id=st.session_state.bulk_edit_csv[st.session_state.book_bulk_ID][i]

                if st.session_state.um.get_unique_user("id",n_id)==None and st.session_state.um.get_unique_user("name",st.session_state.bulk_edit_csv[st.session_state.book_bulk_Title][i])==None:
                    st.session_state.bm.new_book_write(
                        n_id,
                        st.session_state.bulk_edit_csv[st.session_state.book_bulk_Title][i],
                        st.session_state.bulk_edit_csv[st.session_state.book_bulk_Author][i],
                        st.session_state.bulk_edit_csv[st.session_state.book_bulk_Publish_Date][i],
                        st.session_state.bulk_edit_csv[st.session_state.book_bulk_Price][i],
                    )
                else:
                    print(st.session_state.bulk_edit_csv[st.session_state.book_bulk_Title][i]," Already Exists")
