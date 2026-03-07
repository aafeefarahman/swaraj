
import streamlit as st
import pandas as pd
import re
from io import StringIO

def clean_dataframe(df):
    df = df.drop_duplicates()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).apply(clean_text)
    return df

st.set_page_config(page_title="Data Cleaning - Swarjya Hub", layout="wide")
st.title("🧹 Data Cleaning")
st.write("Upload your CSV or text file. Remove duplicates, fix typos, drop noise, and download the cleaned data.")

uploaded_file = st.file_uploader("Upload CSV or TXT file", type=["csv", "txt"])
if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("Preview:", df.head())
        if st.button("Clean Data"):
            cleaned_df = clean_dataframe(df)
            st.success("Data cleaned!")
            st.dataframe(cleaned_df)
            csv = cleaned_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Cleaned CSV", data=csv, file_name="cleaned_data.csv", mime="text/csv")
    elif uploaded_file.name.endswith('.txt'):
        text = StringIO(uploaded_file.getvalue().decode('utf-8')).read()
        st.write("Preview:", text[:500])
        if st.button("Clean Data"):
            cleaned_text = clean_text(text)
            st.success("Text cleaned!")
            st.text_area("Cleaned Text", cleaned_text, height=200)
            st.download_button("Download Cleaned TXT", data=cleaned_text, file_name="cleaned_data.txt", mime="text/plain")
else:
    st.info("Upload a CSV or TXT file to begin cleaning.")

st.divider()
st.caption("© 2025 Swarjya Hub • Data Cleaning Tool")
