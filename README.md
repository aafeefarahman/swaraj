# 🇮🇳 Swarajya: AI-Powered Government Portal Translator

### 🧠 Tagline: *"Bridging Bharat with Bharosa: Making Government Information Truly Accessible."*

---

## 📌 Overview

**Swarajya** is a cloud-native web application designed to make Indian government websites more inclusive and accessible. Despite Hindi and English being official languages, a vast population relies on regional languages and struggles with formal English used in official portals.

Swarajya addresses this language barrier by scraping content from government sites, translating it into user-friendly regional languages, and providing optional voice-based accessibility.

---

## 🎯 Purpose

- To break down complex government English into understandable regional languages.
- To ensure that every citizen, regardless of literacy or language, can access critical schemes, policies, and rights.
- To assist marginalized communities with simplified and translated information delivery.

---

## ✨ Key Features

- 🔎 **Automated Web Scraping** of government website content
- 🌐 **Multi-language Translation** (English ↔ Hindi, Urdu, Telugu, etc.)
- 🗣️ **Text-to-Speech (TTS)** and **Speech-to-Text (STT)** for inclusive voice access
- 🧠 **Content Type Classifier** (e.g., blog, news, about, survey)
- ✨ **Summarization & Grammar Checking** for clarity
- 🖥️ **Minimal UI** for smooth user experience (via Streamlit)

---

## 🛠️ Tech Stack

- **Backend:** Python (NLP, Translation, TTS/STT)
- **Frontend:** Streamlit
- **Libraries:** 
  - `transformers`, `langdetect`, `nltk`, `gTTS`, `SpeechRecognition`
  - `BeautifulSoup`, `requests`, `pandas`, `matplotlib`
- **Deployment:** Local + (Future: Streamlit Cloud / Railway)

---

## 👥 Team Roles

- 👨‍💻 **Sai Mohan & Uday** – Web Scraping Engineers  
  > Building scraping scripts and sourcing data from official government portals.

- 💡 **Shyam Cheni** – Translation, TTS/STT, Frontend Developer, Coordinator  
  > Leads the app integration, voice module, and UI design.

- 📊 **Deepthi & Bindu** – Corpus & Dataset Managers  
  > Curate multilingual datasets for training/testing translation models.

- 📝 **Afeefa** – Documentation & DevOps  
  > Maintains project structure, writes docs, and handles local deployment testing.

---

## 🚀 How to Run the Project Locally

```bash
# Clone the repository
git clone https://github.com/your-org/swarajya.git
cd swarajya

# Install requirements
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
