<<<<<<< HEAD
# 🌐 Swarjya — AI-Powered Government Portal Translator

**Team Name:** Swarjya Team  
**Internship:** Swecha SOAI 2025 — Open Source AI Powered Apps  
**App LINK :** https://swarajya-hub.shyamcheni.workers.dev/

**Repository:** https://code.swecha.org/shyamcheni/swarjya

---

## 👥 Team Members

| Name          | GitLab Username  | Role |
|---------------|------------------|------|
| Shyam Cheni   | shyamcheni        | Coordinator, Frontend, Translation/TTS , All Tools|
| Afeefa         | Afeefa           | Documentation  |
| Deepthi        | Deepthi_ch       | Corpus Data collector |
| Uday           | Uday222          | Web Scraping Engineer |
| Sai Mohan      | sai_mohan        | Web Scraping & QA |

---

## 📜 Project Overview
Swarjya is an **open-source Streamlit application** designed to make government portal content accessible to every citizen, regardless of language barriers.  
The application:
- Scrapes formal English content from government portals.
- Translates it into local Indian languages using AI.
- Provides **Text-to-Speech (TTS)** for accessibility.
- Collects original + translated text pairs for building Indic language corpora.

---

## 🛠 Problem Statement
Many government websites publish information in **formal English**, which is difficult for a large portion of the population to understand.  
This leads to:
- Exclusion from public services.
- Poor awareness of rights and schemes.
- Dependence on intermediaries.

**Swarjya solves this** by offering translation, TTS, and corpus collection to improve accessibility.

---

## 🚀 Features
- **URL Input:** Paste any government portal link.
- **Web Scraper:** Extracts clean readable text from the given page.
- **AI Translation:** English → Local language (Telugu, Hindi, Bengali, Tamil, Malayalam, Gujarati).
- **TTS Support:** Listen to translations instantly.
- **Corpus Export:** Stores original & translated text for NLP research.
- **Offline-first Planning:** Future-ready design for low-connectivity areas.

---

## 📂 Tech Stack
- **Frontend/UI:** Streamlit
- **Backend/Processing:** Python 3.11+, Requests, BeautifulSoup
- **Translation Engine:** AI4Bharat IndicTrans2 API (or offline fallback)
- **Text-to-Speech:** pyttsx3 / gTTS
- **Data Storage:** CSV corpus collection
- **Version Control:** Git + GitLab
- **Deployment:** Streamlit Cloud (Planned)

---

## 📐 Architecture Overview
1. **User Interface (Streamlit)**
   - URL input
   - Language selection
   - Translate & TTS buttons
2. **Web Scraping Module**
   - Fetch HTML
   - Extract readable text
3. **Translation Module**
   - Send text to IndicTrans2 API
   - Receive translated text
4. **TTS Module**
   - Convert translated text to speech
5. **Corpus Logger**
   - Save source & target text pairs into CSV

---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://code.swecha.org/shyamcheni/swarjya.git
cd swarjya


# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app (always start from the welcome page)
streamlit run pages/welcome.py
=======
## Dataset Contribution

We added a small sample dataset of government-related English sentences translated into Telugu and Hindi.  
This dataset is stored in `corpus/dataset_v1.csv` (and `corpus/corpus.json`).  

✅ Purpose:  
- To bootstrap the app with sample translations.  
- To provide a base dataset for future fine-tuning of translation models.  

✅ How it works:  
- Sample dataset can be used locally for development.  
- Export/Import scripts allow fetching translation history from Firebase and saving into CSV/JSONL for analysis.
>>>>>>> deepthi/main
