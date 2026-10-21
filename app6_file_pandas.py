import streamlit as st
import pandas as pd

st.title("Upload CSV and Analyze")

file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if file:
    df = pd.read_csv(file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Filter by Column")

    col = st.selectbox(
        "Choose column",
        df.columns
    )

    value = st.text_input("Filter value")

    if value:
        filtered = df[
            df[col].astype(str).str.contains(
                value,
                case=False
            )
        ]

        st.dataframe(filtered)