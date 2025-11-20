import streamlit as st
import CSVData as csvdat
import io

st.session_state.file_uploaded=False

@st.dialog("Error with File")
def file_error():
    st.write("Error has occuredEnsure File is .csv and then retry")

with st.container(horizontal_alignment="center"):
    if not st.session_state.file_uploaded:
        with st.container(horizontal="center",key="fp_upload_contain",vertical_alignment="center"):
            st.file_uploader("File Upload .csv",key="csv_fp_upload",type="csv")

            st.button("Submit File",key="submit_csv")

            if st.session_state.submit_csv:
                if not st.session_state.csv_fp_upload==None:
                    st.session_state.bulk_edit_csv=csvdat.CSVData(io.StringIO(st.session_state.csv_fp_upload.getvalue().decode("utf-8")).read())

                    st.session_state.file_uploaded=True
                    st.rerun()
                else:
                    file_error()
