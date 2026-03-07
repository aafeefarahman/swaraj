import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("dataset4.csv")

# Clean column names (remove spaces/BOM, standardize case)
df.columns = df.columns.str.strip()           # remove leading/trailing spaces
df.columns = df.columns.str.replace('\ufeff', '')  # remove BOM if present
df.columns = df.columns.str.title()           # make consistent: Title, English, Telugu, Hindi

# Set Streamlit title
st.title("Translation Viewer - English | Telugu | Hindi")

# Dropdown to select a title
selected_title = st.selectbox("Select a Topic", df['Title'])

# Find the row that matches the selected title
row = df[df['Title'] == selected_title].iloc[0]

# Show translations
st.subheader("Translations:")
st.markdown(f"**English**: {row['English']}")
st.markdown(f"**Telugu**: {row['Telugu']}")
st.markdown(f"**Hindi**: {row['Hindi']}")
