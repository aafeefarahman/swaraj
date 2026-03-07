import streamlit as st
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

st.set_page_config(page_title="Vectorizing - Swarjya Hub", layout="wide")
st.title("🔢 Vectorizing")
st.write("Convert text into vectors (One-hot encoding / Bag of Words).")

# User input
text = st.text_area("Enter text (one line per entry):", height=200)
method = st.selectbox("Choose vectorization method:", ["One-hot (Bag of Words)"])

if text:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    if method == "One-hot (Bag of Words)":
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(lines)

        st.write("### Vocabulary")
        st.write(vectorizer.get_feature_names_out())

        st.write("### Vectors")
        st.dataframe(X.toarray())

        st.download_button(
            "Download Vectors (CSV)",
            data=np.array2string(X.toarray(), separator=','),
            file_name="vectors.csv",
            mime="text/csv"
        )
else:
    st.info("Enter text and select a method to vectorize.")

st.divider()
st.caption("© 2025 Swarjya Hub • Vectorizing Tool")
