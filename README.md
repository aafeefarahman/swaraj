---

# Swarjya

Swarjya is an open-source application developed during the **Swecha SOAI 2025 – Open Source AI Powered Apps Internship**.
The project aims to make government portal information easier to understand by translating complex English content into **regional Indian languages**.

The system also supports **Text-to-Speech (TTS)** so users can listen to translated content. In addition, the project collects translation pairs that can help build **Indic language datasets for NLP research**.

---

# 1. Project Overview

Many government websites publish important information in formal English, which can be difficult for many citizens to understand.

Swarjya helps address this issue by:

* Extracting readable content from government portal webpages
* Translating the content into local Indian languages
* Providing audio output using Text-to-Speech
* Collecting original and translated text pairs for dataset creation

This helps improve **information accessibility and language inclusivity**.

---

# 2. Problem Statement

Government portals often contain important information related to schemes, policies, and public services. However, the use of complex English can create barriers for many people.

Some challenges include:

* Limited awareness of government schemes
* Difficulty understanding official information
* Dependence on intermediaries for explanations

Swarjya aims to bridge this gap using **AI-powered translation and speech technologies**.

---

# 3. Key Features

• **URL Input**

* Users can paste a government portal link.

• **Web Scraping**

* Extracts readable text from webpages.

• **AI Translation**

* Translates English content into Indian languages.

Supported languages:

* Telugu
* Hindi
* Bengali
* Tamil
* Malayalam
* Gujarati

• **Text-to-Speech**

* Converts translated text into speech for better accessibility.

• **Corpus Collection**

* Stores translation pairs that can be used to build datasets for NLP research.

---

# 4. Technology Stack

• **Frontend**

* Streamlit

• **Backend**

* Python

• **Libraries**

* Requests
* BeautifulSoup

• **Translation Engine**

* AI4Bharat IndicTrans2 API

• **Text-to-Speech**

* pyttsx3
* gTTS

• **Data Storage**

* CSV files for corpus collection

• **Version Control**

* Git

---

# 5. Project Architecture

The application works through the following steps:

1. **User Interface**

   * User enters a government portal URL.
   * Selects the target language.

2. **Web Scraping Module**

   * Fetches webpage HTML.
   * Extracts readable content.

3. **Translation Module**

   * Sends text to the translation API.
   * Receives translated output.

4. **Text-to-Speech Module**

   * Converts translated text into audio.

5. **Corpus Logger**

   * Saves both source and translated text pairs for dataset building.

---

# 6. Installation and Setup

1️⃣ Clone the repository

```bash
git clone https://github.com/aafeefarahman/swaraj.git
cd swaraj
```

2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

3️⃣ Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

5️⃣ Run the application

```bash
streamlit run pages/welcome.py
```

---

# 7. Dataset Contribution

A small dataset of government-related English sentences translated into **Telugu and Hindi** has been included.

Dataset location:

```
corpus/dataset_v1.csv
corpus/corpus.json
```

Purpose:

* Provide sample translation pairs
* Support creation of Indic language NLP datasets
* Help future fine-tuning of translation models

---
---

## 8. Project Structure

This helps people quickly understand the repo layout.

Example:

```
swaraj/
│
├── pages/                # Streamlit UI pages
├── corpus/               # Dataset and translation corpus
├── scraped_data/         # Scraped website content
├── translator-proxy/     # Translation service integration
├── utils/                # Helper scripts
├── extension/            # Browser extension related files
├── Document/             # Project documentation
├── requirements.txt      # Project dependencies
└── README.md             # Project overview
```


## 9. Use Cases / Applications
* Making government schemes easier to understand
* Helping rural users access official information
* Supporting multilingual digital governance
* Building datasets for Indic NLP research
* Improving accessibility through speech support

---


## 10. Future Improvements
* Support more Indian languages
* Improve translation accuracy
* Add offline translation support
* Improve UI and accessibility features
* Expand the dataset for better NLP training

---


