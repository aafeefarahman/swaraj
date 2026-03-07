import streamlit as st
import re
import string

st.set_page_config(page_title="Normalizing - Swarjya Hub", layout="wide")
st.title("🔄 Normalizing")
st.write("Lowercase, remove punctuation, and normalize your text for AI/ML.")

# User input
text = st.text_area("Enter text to normalize:", height=200)

if text:
    normalized = text.lower()
    normalized = normalized.translate(str.maketrans('', '', string.punctuation))
    normalized = re.sub(r'\s+', ' ', normalized).strip()

    st.subheader("Normalized Text")
    st.text_area("Result", normalized, height=200)

    st.download_button(
        "Download Normalized Text",
        data=normalized,
        file_name="normalized.txt",
        mime="text/plain"
    )
else:
    st.info("Enter text above to normalize.")

st.divider()
st.caption("© 2025 Swarjya Hub • Normalizing Tool")
