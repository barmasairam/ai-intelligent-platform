import streamlit as st
import pandas as pd
from main import handle_query

st.title("🚀 Intelligent AI Platform")

query = st.text_input("Ask your question:")

if query:
    result = handle_query(query)

    if result["type"] == "sql":
        df = pd.DataFrame(result["data"])
        st.dataframe(df)

    else:
        st.metric("Predicted Sales", result["prediction"])

    st.success(result["insight"])