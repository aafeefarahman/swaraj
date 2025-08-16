
---

# Swaraj: AI-Powered Government Portal Translator
**Bridging Bharat with Bharosa: Making Government Information Truly Accessible**

---

## **1. Project Overview / Abstract**

Swaraj is an **AI-powered Streamlit web application** designed to make official government content accessible in **regional Indian languages** like Hindi, Urdu, and Telugu.

It **bridges the language divide** by translating formal English text from government portals, while also providing **voice accessibility** and **readable content**, ensuring governance is truly inclusive.

---

## **2. Motivation / Purpose**

* **Inclusivity:** Millions of Indians rely on regional languages to access information.
* **Accessibility:** Complex English and formal website structures make it hard for non-English speakers.
* **Empowerment:** By simplifying government content, citizens can better **understand policies, exercise rights, and access services**.

> Swaraj is designed not only to translate text but also to **speak and listen**, making government portals interactive for all citizens.

---

## **3. Key Features**

* 🗂️ **Scraping Engine:** Extracts structured content (paragraphs, headings) from government websites.
* 🌐 **Translation Module:** Converts scraped text to Hindi, Urdu, Telugu.
* 🗣️ **Text-to-Speech (TTS):** Reads translations aloud.
* 🎤 **Speech-to-Text (STT):** Accepts user voice input for queries.
* 💾 **Corpus Creation:** Builds datasets for AI research and fine-tuning.
* 🖥️ **Minimal UI:** Clean, simple Streamlit interface.
* 🧪 **Rapid Testing:** Quick prototyping and deployment.

---

## **4. Tech Stack**

* **Backend:** Python (NLP, translation, TTS/STT)
* **Frontend:** Streamlit
* **Libraries:** BeautifulSoup, requests, pandas, transformers, langdetect, nltk, gTTS, SpeechRecognition
* **Database:** SQLite / Firebase
* **Deployment:** Local environment & Streamlit Cloud

---

## **5. Team Roles**

| Member           | Role                                        | Responsibility                                                       |
| ---------------- | ------------------------------------------- | -------------------------------------------------------------------- |
| Sai Mohan & Uday | Web Scraping Engineers                      | Build scraping scripts and source data from government portals       |
| Shyam Cheni      | Translation, TTS/STT, Frontend, Coordinator | Leads app integration, voice module, and UI design                   |
| Deepthi & Bindu  | Corpus & Dataset Managers                   | Curate multilingual datasets for training/testing translation models |
| Afeefa           | Documentation & DevOps                      | Maintains project structure, writes docs, deployment testing         |

---

## **6. Installation & Setup**

### **Step 1 — Install Python 3.11+**

```bash
python --version
# If not installed:
# Windows / Mac: download from https://www.python.org/downloads/
# Linux:
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip
```

---

### **Step 2 — Clone Repository**

```bash
git clone https://github.com/your-username/swaraj.git
cd swaraj
```

---

### **Step 3 — Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows
```

---

### **Step 4 — Install Dependencies**

```bash
pip install -r requirements.txt
# If missing:
pip install streamlit googletrans==4.0.0rc1 gTTS SpeechRecognition pandas requests beautifulsoup4
```

---

### **Step 5 — Run Streamlit App**

```bash
streamlit run app.py
```

---

## **7. Data Pipeline Documentation**
<img width="409" height="1501" alt="image" src="https://github.com/user-attachments/assets/fcd7abad-6b6a-410d-89d1-af6d455f3132" />

Swaraj’s data flow is designed for **clarity, reusability, and robustness**:

1. **User Input:** Paste government portal URL in Streamlit.
2. **Web Scraping:**

   * `scraper.py` extracts **paragraphs, headings**, removes ads/footers.
   * Output stored in JSON:

     ```json
     {
       "url": "https://...",
       "title": "Page Title",
       "content": "Clean paragraph content here"
     }
     ```
   * Sample command:

     ```bash
     python scraper.py --url "https://www.india.gov.in"
     ```
3. **Translation Module:** Converts text to selected language using `translator.py`.

   * Sample command:

     ```bash
     python translator.py --input data/sample.json --lang hi
     ```
4. **TTS/STT:**

   * Speak translations:

     ```bash
     python tts.py --text "Namaste" --lang hi
     ```
   * Voice input captured via STT module for queries.
5. **Corpus Storage:**

   * Original + translated text saved in `/data` folder and DB:

     ```bash
     sqlite3 swaraj.db
     ```
6. **Display:** Clean text displayed in Streamlit UI.

---

## **8. Pipeline Refinements & Optimizations**

During Sprint 1-2, several **improvements were made**:

* **Scraper Optimization:**

  * Removed unnecessary HTML tags (ads, headers, footers).
  * Handled **timeouts** and **invalid URLs** gracefully.
  * Chunked long text into smaller segments for smooth translation.
* **Translation Improvements:**

  * Verified accuracy for Hindi, Urdu, Telugu manually.
  * Stored translations in structured CSV:

    ```csv
    title,english,hindi,urdu,telugu
    ```
* **Corpus Export Script:** Automated conversion of DB entries to text files for AI training.

  ```bash
  python export_corpus.py --output data/corpus_v1.txt
  ```

---

## **9. Deployment Guide**

### **Local Deployment**

1. Ensure Python 3.11+, virtual environment, and dependencies installed.
2. Run the app:

   ```bash
   streamlit run app.py
   ```
3. Access locally at `http://localhost:8501`.

---

### **Streamlit Cloud Deployment**

1. Push code to GitHub repository:

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. Login to [Streamlit Cloud](https://share.streamlit.io/) and connect the repo.
3. Configure Python 3.11 environment and `requirements.txt`.
4. Deploy and access via public URL.

---

## **10. Challenges Faced**

* Handling **dynamic content** on government portals (ads, inconsistent HTML).
* Chunking large texts for translation to avoid API errors.
* Ensuring **voice modules** worked offline (pyttsx3) and online (gTTS).
* Testing **local deployment reproducibility** across machines.
* Installing streamlit & learning it.

---

## **11. Future Work**

* Add **chatbot** summarization for pages.
* Extend **language support** beyond Hindi, Urdu, Telugu.
* Enhance **grammar correction** and **AI summarization**.
* Public cloud hosting with persistent database for citizens.

---


---


