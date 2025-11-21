import streamlit as st
import BookManager
from Book import Book

"""
Blank table
What each of the columns are
get id, then value, then new value
"""

import pandas as pd

with st.container(horizontal_alignment="center"):
    confusion_matrix = pd.DataFrame(
        {
            "Predicted Cat": [85, 3, 2, 1],
            "Predicted Dog": [2, 78, 4, 0],
            "Predicted Bird": [1, 5, 72, 3],
            "Predicted Fish": [0, 2, 1, 89],
        },
        index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"],
    )
    st.table(confusion_matrix, border="horizontal")



