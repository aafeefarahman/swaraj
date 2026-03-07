import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io
import requests
from bs4 import BeautifulSoup
from firebase_utils import save_translation_to_firestore
from streamlit_lottie import st_lottie
import json

# ---------- CONFIG ----------
LANGS = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "te": "Telugu",
    "es": "Spanish"
}

st.set_page_config(
    page_title="Swarjya — Translate & Speak",
    layout="centered",
    page_icon="🌐"
)

# ---------- HEADER ----------
st.markdown(
    """
    <style>
    h1 {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #ff4b4b;
    }
    .stButton button {
        border-radius: 10px;
        background-color: #ff4b4b !important;
        color: white !important;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #ff6f6f !important;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌐 Swarjya")
st.subheader("Goverment Portal Translator")

# ---------- INPUT SELECTION ----------
input_type = st.radio("📥 Choose input type", ["✏️ Text", "🔗 URL"], index=0, horizontal=True)

if input_type == "✏️ Text":
    user_text = st.text_area("📝 Paste text to translate", height=180, placeholder="Enter your text here...")
else:
    user_text = st.text_input("🌍 Enter page URL", placeholder="https://example.com")

# ---------- LANGUAGE PICKER ----------
target = st.selectbox("🌎 Target language", [f"{code} — {name}" for code, name in LANGS.items()])

# ---------- BUTTONS ----------
col1, col2 = st.columns(2)

if col1.button("🚀 Translate"):
    if not user_text:
        st.warning("⚠️ Please enter some text or a valid URL.")
    else:
        with st.spinner("✨ Translating..."):
            try:
                if input_type == "🔗 URL" and user_text.startswith(("http://", "https://")):
                    r = requests.get(user_text, timeout=8)
                    soup = BeautifulSoup(r.content, "html.parser")
                    text = " ".join(p.get_text() for p in soup.find_all("p"))
                    text = text[:4000] or (soup.get_text()[:4000])
                else:
                    text = user_text

                tgt_code = target.split(" — ")[0]
                translated = GoogleTranslator(source="auto", target=tgt_code).translate(text)

                save_translation_to_firestore(
                    source_text=text,
                    translated_text=translated,
                    source_lang="auto",
                    target_lang=tgt_code
                )

                st.session_state["translated_text"] = translated
                st.success("✅ Translation complete!")
                st.text_area("📜 Translated text", translated, height=220)
            except Exception as e:
                st.error(f"❌ Translation failed: {e}")

if col2.button("🔊 Speak"):
    if "translated_text" not in st.session_state:
        st.warning("⚠️ Translate text first.")
    else:
        with st.spinner("🎙️ Generating speech..."):
            try:
                tgt_code = target.split(" — ")[0]
                tts = gTTS(st.session_state["translated_text"], lang=tgt_code)
                mp3_buf = io.BytesIO()
                tts.write_to_fp(mp3_buf)
                mp3_buf.seek(0)
                st.audio(mp3_buf.read(), format="audio/mp3")
            except Exception as e:
                st.error(f"❌ TTS failed: {e}")

# ---------- FOOTER ----------
st.markdown(
    "<p style='text-align:center; color:gray; font-size:0.9rem;'>Made with ❤️ by Shyam</p>",
    unsafe_allow_html=True
)
