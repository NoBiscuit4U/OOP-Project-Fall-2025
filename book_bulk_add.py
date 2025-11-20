import streamlit as st
import CSVData as csvdat

st.session_state.file_uploaded=False

@st.dialog("Error with File")
def file_error():
    st.write("Ensure File is .csv and then retry")

with st.container(horizontal_alignment="center"):
    with st.container(horizontal="center",key="fp_upload_contain"):
        st.file_uploader(".csv File Upload",key="csv_fp_upload",type="csv")

        st.button("Submit File",key="submit_csv")

        if not st.session_state.csv_fp_upload==None:
            st.session_state.bulk_edit_csv=csvdat.CSVData(st.session_state.csv_fp_upload)

            st.session_state.file_uploaded=True
            st.rerun()
        else:
            file_error()