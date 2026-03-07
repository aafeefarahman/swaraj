import streamlit as st
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import base64
import time
from urllib.parse import urlparse

# =========================
#  CONFIG — must be first
# =========================
st.set_page_config(
    page_title="Swarjya — Webpage Translator", 
    layout="wide", 
    page_icon="🌐"
)

# Remove sidebar completely
st.markdown("""
    <style>
    .css-1d391kg {display: none;}
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-radius: 0.5rem;
        border-left: 5px solid #28a745;
        margin-bottom: 1.5rem;
    }
    .website-info {
        padding: 1rem;
        background-color: #e9ecef;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .section-box {
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        border-left: 3px solid #6f42c1;
        margin-bottom: 1rem;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------- Utils -------------
def normalize_url(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("www."):
        raw = "https://" + raw
    if not raw.startswith(("http://", "https://")):
        raw = "https://" + raw
    return raw

@st.cache_data(show_spinner=False, ttl=600)
def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch URL: {e}")
        return None

def extract_sections(html: str):
    if not html:
        return "No Title", []
        
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
        tag.decompose()

    page_title = (soup.title.string.strip() if soup.title and soup.title.string else "Untitled")
    flow_tags = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "div"]
    nodes = soup.find_all(flow_tags)

    sections = []
    current = {"heading": page_title, "blocks": []}

    for el in nodes:
        name = el.name.lower()
        text = " ".join(el.get_text(separator=" ", strip=True).split())
        if not text or len(text) < 10:
            continue

        if name.startswith("h") and name[1:].isdigit() and int(name[1:]) < 4:
            if current["blocks"]:
                sections.append(current)
            current = {"heading": text, "blocks": []}
        elif name == "li":
            current["blocks"].append(f"• {text}")
        else:
            if len(text) > 30 or (el.find_all("p") and not el.find_all("div")):
                current["blocks"].append(text)

    if current["blocks"]:
        sections.append(current)

    return page_title, sections

def translate_sections(sections, target="te"):
    if not sections:
        return []
        
    translator = GoogleTranslator(source="auto", target=target)
    translated = []

    for sec in sections:
        try:
            t_heading = translator.translate(text=sec["heading"])
        except Exception:
            t_heading = sec["heading"]

        translated_blocks = []
        for block in sec["blocks"]:
            try:
                if len(block) > 4500:
                    parts = [block[i:i+4500] for i in range(0, len(block), 4500)]
                    translated_parts = [translator.translate(part) for part in parts]
                    translated_block = " ".join(translated_parts)
                else:
                    translated_block = translator.translate(block)
            except Exception:
                translated_block = block
            translated_blocks.append(translated_block)
            
        translated.append({"heading": t_heading, "blocks": translated_blocks})
        time.sleep(0.1)
        
    return translated

def render_sections(sections, show_toc=True):
    if not sections:
        st.warning("No content sections found to display.")
        return
        
    if show_toc:
        st.markdown("### 📑 Table of Contents")
        for i, sec in enumerate(sections, start=1):
            st.markdown(f"- [{sec['heading']}](#sec-{i})")
        st.markdown("---")

    for i, sec in enumerate(sections, start=1):
        st.markdown(f"<div class='section-box'>", unsafe_allow_html=True)
        st.markdown(f"<h2 id='sec-{i}'>{sec['heading']}</h2>", unsafe_allow_html=True)
        for b in sec["blocks"]:
            if b.startswith("• "):
                st.markdown(b)
            else:
                st.write(b)
        st.markdown("</div>", unsafe_allow_html=True)

def build_translated_html(title, sections, source_url):
    html = f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>{title} - Translated</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 1000px; margin: 0 auto; }}
            h1 {{ color: #1f77b4; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
            h2 {{ color: #ff7f0e; margin-top: 30px; }}
            .source-info {{ background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <div class="source-info">
            <strong>Source Website:</strong> {urlparse(source_url).netloc}<br>
            <strong>Hyper Link:</strong> <a href="{source_url}" target="_blank">{source_url}</a><br>
            <strong>Translated on:</strong> {time.strftime("%Y-%m-%d %H:%M:%S")}
        </div>
    """
    
    for i, sec in enumerate(sections, start=1):
        html += f"<h2 id='sec-{i}'>{sec['heading']}</h2>"
        for b in sec["blocks"]:
            html += f"<p>{b}</p>"
    
    html += "</body></html>"
    return html

def get_domain_info(url):
    parsed = urlparse(url)
    return {"full_url": url, "domain": parsed.netloc, "protocol": parsed.scheme}

# =========================================
#  PAGE: MAIN — Scrape → Translate
# =========================================
st.markdown("<h1 class='main-header'>🌐 Swarjya — Webpage Translator</h1>", unsafe_allow_html=True)
st.caption("Target URL → Scrape → Translate → Rearranged layout.")

language_options = {
    "te": "Telugu","hi": "Hindi","en": "English","fr": "French","es": "Spanish",
    "de": "German","ja": "Japanese","ru": "Russian","ar": "Arabic","pt": "Portuguese",
    "bn": "Bengali","ta": "Tamil"
}

col1, col2 = st.columns([3, 1])
with col1:
    default_url = st.session_state.get("url_input", "")
    url_input = st.text_input("Enter a webpage URL", value=default_url, placeholder="https://www.pmindia.gov.in/")
with col2:
    selected_lang = st.selectbox("Target Language",
        options=list(language_options.keys()),
        format_func=lambda x: f"{x} — {language_options[x]}",
        key="lang_select")

if st.button("🔍 Scrape & Translate", type="primary", use_container_width=True):
    if not url_input.strip():
        st.warning("Please enter a URL.")
    else:
        try:
            url = normalize_url(url_input)
            domain_info = get_domain_info(url)
            
            google_translated_url = (
                f"https://translate.google.com/translate?hl={selected_lang}&sl=auto&u={domain_info['full_url']}"
            )

            st.markdown("<div class='website-info'>", unsafe_allow_html=True)
            st.markdown(f"**Source Website:** {domain_info['domain']}")
            st.markdown(
                f"""**Hyper Link:** <a href="{google_translated_url}" target="_blank">{domain_info['full_url']}</a>""",
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)
            
            with st.spinner(f"Fetching content from: {url}..."):
                html = fetch_html(url)
                if html is None:
                    st.error("Failed to retrieve content from the URL. Please check the URL and try again.")
                    st.stop()
                title, sections = extract_sections(html)
                if not sections:
                    st.warning("No meaningful content could be extracted from this page.")
                    st.stop()
                with st.spinner(f"Translating to {language_options[selected_lang]}..."):
                    t_sections = translate_sections(sections, target=selected_lang)

            st.markdown("<div class='success-box'>", unsafe_allow_html=True)
            st.success(f"✅ Translation complete! Displaying content from: {title}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            translated_html = build_translated_html(title, t_sections, url)
            st.markdown("### ✅ Rearranged & Translated Content")
            render_sections(t_sections, show_toc=True)

            col1, col2 = st.columns(2)
            with col1:
                st.download_button("💾 Download Translated Page",
                    data=translated_html,
                    file_name=f"translated_{domain_info['domain']}.html",
                    mime="text/html",
                    use_container_width=True)
            with col2:
                st.markdown(
                    f'<a href="{google_translated_url}" target="_blank" '
                    f'style="display:inline-block;width:100%;padding:0.5rem 1rem;'
                    f'background-color:#4CAF50;color:white;text-align:center;'
                    f'text-decoration:none;border-radius:0.3rem;">🌍 Open Website in {language_options[selected_lang]}</a>',
                    unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Failed to process URL: {str(e)}")

if st.button("🏠 Back to Home"):
    st.switch_page("home.py")

st.markdown("---")
st.caption("Swarjya Web Translator • Extract, translate, and view web content in your preferred language")
