import streamlit as st

st.set_page_config(page_title="Swarjya Hub - AI Web Tools", layout="wide")

# ==== HEADER ====
col1, col2, col3 = st.columns([1, 5, 2])

with col1:
    st.image("swaraj.png", width=50)  # logo

with col2:
    st.title("Swarjya Hub")

# Removed login/signup buttons completely
# with col3:
#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button("🔑 Login", use_container_width=True):
#             st.switch_page("pages/2_🔑_Login.py")
#     with c2:
#         if st.button("📝 Create Account", use_container_width=True):
#             st.switch_page("pages/3_📝_Signup.py")

st.subheader("AI Tools for Web Translation, Data Scraping, and Corpus Collection")
st.write(
    "Welcome to **Swarjya Hub**, your one-stop AI hub for innovators and developers. "
    "Translate web pages, scrape data, build corpora, and even label unstructured datasets."
)

st.divider()

# ==== HIGHLIGHTS ====
st.subheader("✨ Highlights")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("AI Translation", "Multilingual", "+ Context Preserved")
with c2:
    st.metric("Web Scraper", "Structured Data", "→ Export Formats")
with c3:
    st.metric("Corpus & Labeling", "Datasets", "📊 Ready for AI")

st.divider()

# ==== TOOLS GRID ====
st.subheader("🚀 Tools")

tools = [
    {
        "title": "📝 Basic Language Translator",
        "desc": "Translate text between languages easily.",
        "page": "pages/Translator.py",
    },
    {
        "title": "🌍 Webpage Translator",
        "desc": "Translate entire web pages while keeping layout & meaning.",
        "page": "app.py",
    },
    {
        "title": "📊 Web Scraper",
        "desc": "Extract structured data from websites, export in multiple formats.",
        "page": "webscraper.py",
    },
    {
        "title": "📚 Corpus Collector",
        "desc": "Collect, clean and manage text datasets for AI training.",
        "page": "pages/corpus.py",
    },
    {
        "title": "🧹 Data Cleaning",
        "desc": "Remove duplicates, fix typos, drop noise from your data.",
        "page": "pages/clean.py",
    },
    {
        "title": "🏷️ Label Data",
        "desc": "Convert unlabelled text into labelled datasets for ML models.",
        "page": "pages/labeldata.py",
    },
    {
        "title": "🔤 Tokenizing",
        "desc": "Break text into words/tokens.",
        "page": "pages/tokenizing.py",
    },
    {
        "title": "🔄 Normalizing",
        "desc": "Lowercase, remove punctuation, etc.",
        "page": "pages/normalizing.py",
    },
    {
        "title": "🔢 Vectorizing",
        "desc": "Convert words/images into numbers (embeddings, one-hot, etc.).",
        "page": "pages/vectorizing.py",
    },
]

cols = st.columns(2)

for i, tool in enumerate(tools):
    with cols[i % 2]:
        with st.container(border=True):
            st.markdown(f"### {tool['title']}")
            st.write(tool["desc"])
            # Removed sign-in check
            if st.button(f"Go to {tool['title']}", key=tool["title"], use_container_width=True):
                st.switch_page(tool["page"])

st.divider()

# ==== FOOTER ====
st.caption("© 2025 Swarjya Hub • AI Web Translator, Scraper, Corpus & Labeling Tools • Built for Innovators 🚀")
