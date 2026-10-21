import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Visualization")

# Sample data
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Math", "Science", "English"]
)

st.subheader("Built-in Charts")

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.subheader("Matplotlib Chart")

fig, ax = plt.subplots()

ax.hist(
    df["Math"],
    bins=10,
    color="skyblue"
)

ax.set_title("Math Score Distribution")

st.pyplot(fig)