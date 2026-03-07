
import streamlit as st
import pandas as pd
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
import os

# List of bad words to clean (add more as needed)
bad_words = [
    "fuck",
    "asshole",
    "bitch",
    "bastard",
    "damn",
    "shit",
    "nigga",
    "cunt",
    "dick",
    "piss",
    "prick",
    "slut",
    "whore",
    "fag",
    "motherfucker",
    "twat",
    "cock",
    "arse",
    "bollocks",
    "bugger",
    "wanker",
    "tit",
    "crap",
    "dyke",
    "jerk",
    "moron",
    "idiot",
    "paiki",      # placeholder for a common insult
    "gandu",      # placeholder
    "pichi",      # placeholder
    "buddi",      # placeholder
    "thodu",      # placeholder
    "kukka",      # placeholder
    "chekka",     # placeholder
    "thappu",     # placeholder
    "mokka",      # placeholder
    "dengey",
    "lowda",
    "asshole",
    "motherfucker"       # placeholder


]


# Returns True if text contains any bad word
def contains_bad_words(text):
    lowered = text.lower()
    for word in bad_words:
        if word in lowered:
            return True
    return False

# Path to your downloaded JSON key file (update if needed)
SERVICE_ACCOUNT_PATH = os.path.join("secrets", "swarjya-translator-firebase-adminsdk-fbsvc-f10366303b.json")

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.set_page_config(page_title="Corpus Analyzer - Swarjya Hub", layout="wide")
st.title("📚 Corpus Analyzer")
st.write("Analyze and export your translation corpus from the database.")

if st.button("Fetch Translations from Database"):
    with st.spinner("Fetching data from the database..."):
        docs = db.collection("translations").order_by("timestamp").stream()
        data = []
        for doc in docs:
            d = doc.to_dict()
            source = d.get("source_text", "")
            translated = d.get("translated_text", "")
            # Skip row if any bad word is present in source or translated text
            if contains_bad_words(source) or contains_bad_words(translated):
                continue
            data.append({
                "source_text": source,
                "translated_text": translated,
                "source_lang": d.get("source_lang", ""),
                "target_lang": d.get("target_lang", ""),
                "timestamp": d.get("timestamp", "")
            })
        if data:
            df = pd.DataFrame(data)
            st.success(f"Fetched {len(df)} translations.")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download as CSV", data=csv, file_name="translations.csv", mime="text/csv")

            # Show Graph button (directly from fetched data)
            if st.button("Show Graph"):
                st.subheader("Translations by Source and Target Language")
                if not df.empty and "source_lang" in df.columns and "target_lang" in df.columns:
                    lang_counts = df.groupby(["source_lang", "target_lang"]).size().reset_index(name="count")
                    st.bar_chart(lang_counts.set_index(["source_lang", "target_lang"]))
                else:
                    st.info("No data to display in graph.")
        else:
            st.warning("No translation data found in the database.")
else:
    st.info("Click the button above to fetch and export your translation corpus from the database.")

# List of bad words to clean (add more as needed)
bad_words = ["badword1", "badword2", "badword3"]

def clean_bad_words(text):
    for word in bad_words:
        text = text.replace(word, "***")
    return text

    st.info("Click the button above to fetch and export your translation corpus from the database.")
