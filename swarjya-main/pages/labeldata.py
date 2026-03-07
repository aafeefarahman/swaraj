import streamlit as st
import pandas as pd

def label_text(text, label):
    return {'text': text, 'label': label}

st.set_page_config(page_title="Label Data - Swarjya Hub", layout="wide")
st.title("🏷️ Label Data")
st.write("Convert your unlabelled text into labelled datasets for machine learning.")

st.divider()

# Step 1: Paste unlabelled data
st.subheader("Step 1: Paste Unlabelled Data")
user_text = st.text_area("Paste your unlabelled text here (one entry per line):", height=200)

if user_text:
    lines = [line.strip() for line in user_text.split('\n') if line.strip()]
    st.write(f"**{len(lines)}** entries detected.")

    st.divider()
    st.subheader("Step 2: Assign Labels")

    labelled_data = []
    for i, line in enumerate(lines):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write(line)
        with col2:
            label = st.text_input(f"Label for entry {i+1}", key=f"label_{i}")
        labelled_data.append(label_text(line, label))

    st.divider()
    if st.button("Generate Labelled Data"):
        df = pd.DataFrame(labelled_data)
        st.success("Labelled data generated!")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download as CSV", data=csv,
                           file_name="labelled_data.csv",
                           mime="text/csv")
else:
    st.info("Paste your unlabelled text above to begin labelling.")

st.divider()
st.caption("© 2025 Swarjya Hub • Label Data Tool")
