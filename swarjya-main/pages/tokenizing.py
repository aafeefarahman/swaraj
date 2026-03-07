import streamlit as st
import re

st.set_page_config(page_title="Tokenizing - Swarjya Hub", layout="wide")
st.title("🔤 Tokenizing")
st.write("Break your text into words/tokens for NLP tasks.")

# Text input
text = st.text_area("Enter text to tokenize:", height=200)

if text:
    tokens = re.findall(r'\b\w+\b', text)
    st.write(f"**{len(tokens)} tokens found:**")
    st.code(tokens)

    st.download_button(
        "Download Tokens as TXT",
        data='\n'.join(tokens),
        file_name="tokens.txt",
        mime="text/plain"
    )
else:
    st.info("Enter text above to tokenize.")

st.divider()
st.caption("© 2025 Swarjya Hub • Tokenizing Tool")
