
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
<img width="1352" height="1429" alt="image" src="https://github.com/user-attachments/assets/83695fb0-8d2a-4e11-a062-d9d2921b0172" />
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
---

## **9. Challenges Faced**

* Handling **dynamic content** on government portals (ads, inconsistent HTML).
* Chunking large texts for translation to avoid API errors.
* Ensuring **voice modules** worked offline (pyttsx3) and online (gTTS).
* Testing **local deployment reproducibility** across machines.
* Installing streamlit & learning it.

---
---

## 10. Streamlit Deployment Steps

**1. Install Dependencies**

* Make sure Python (≥3.9) is installed.
* Install project requirements:

  ```bash
  pip install -r requirements.txt
  ```

**2. Set Up Virtual Environment** *(Optional but recommended)*

* Create environment:

  ```bash
  python -m venv venv
  ```
* Activate it:

  * Windows: `venv\Scripts\activate`
  * Linux/Mac: `source venv/bin/activate`

**3. Organize Project Files**

* Keep files in a structured format:

  ```
  /swaraj
    ├── app.py              # Main Streamlit app
    ├── scraper/            # Scraping scripts
    ├── translation/        # Translation pipeline
    ├── data/               # Datasets or cache
    ├── requirements.txt    # Dependencies
    └── README.md
  ```

**4. Run Locally**

* Launch app with:

  ```bash
  streamlit run app.py
  ```
* Open browser at `http://localhost:8501`.

**5. Test Functionality**

* Verify scraping → translation → display works.
* Check UI, buttons, and language output.

**6. Configure GitHub Repository**

* Push code to GitHub repo for deployment.
* Include `.gitignore` to skip cache & venv.

**7. Setup Streamlit Cloud Account**

* Sign in at [streamlit.io](https://streamlit.io).
* Connect with GitHub repository.

**8. Deploy the Application**

* Select the repo & branch.
* Choose the main file (`app.py`).
* Set Python version & requirements.txt.

**9. Configure Secrets (if needed)**

* Add API keys or environment variables securely in Streamlit Cloud → Settings → Secrets.

**10. Verify Online Deployment**

* Open the hosted link provided by Streamlit Cloud.
* Test on multiple devices (mobile, tablet, desktop).

**11. Maintain & Update**

* Update code in GitHub → Auto redeploys on Streamlit Cloud.
* Monitor logs for errors & fix issues.

---

---

### **11. Deployment of Project**

#### **Local Deployment**

The project can be run locally on any machine with Python installed. This is useful for contributors who want to test and experiment with scraping, translation, and the UI in real-time.

**Steps for Local Deployment:**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/swaraj.git
   cd swaraj
   ```

2. **Set Up Virtual Environment (Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate     # For Linux/Mac
   venv\Scripts\activate        # For Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   * The application will start a local server.
   * Open the provided link (default: `http://localhost:8501`) in your browser.

This setup allows contributors to work on **scraping pipelines, translation logic, or UI changes** instantly and test them in their own environment.

---

#### **Streamlit Cloud Deployment**

The project is also deployed on **Streamlit Cloud** for accessibility, collaboration, and easy sharing. Streamlit Cloud automatically takes care of hosting, building, and deploying the app.

**Steps for Streamlit Cloud Deployment:**

1. **Push Code to GitHub**

   * Ensure that the latest code is committed and pushed to the repository (main branch or deployment branch).
   * Example:

     ```bash
     git add .
     git commit -m "Update: Added translation improvements"
     git push origin main
     ```

2. **Link Repository to Streamlit Cloud**

   * Go to [Streamlit Cloud](https://streamlit.io/cloud).
   * Create a new app and link it to your GitHub repository.

3. **Configure Deployment Settings**

   * Select the correct branch (`main` or your chosen branch).
   * Set the **Main file path** (usually `app.py`).
   * Add required **secrets** (API keys, credentials, etc.) in the Streamlit Cloud dashboard under **Secrets Management**.

4. **Automatic Deployment**

   * Every time a new commit is pushed to GitHub, Streamlit Cloud automatically rebuilds and redeploys the app.
   * No manual restart is needed.

5. **Accessing the App**

   * A live URL will be generated (e.g., `https://swaraj.streamlit.app`).
   * Share this link with collaborators, testers, or users.

---
## 12 Future Work

* Add support for more Indian regional languages.
* Implement advanced NLP features (summarization, sentiment analysis).
* Optimize scraping speed with asynchronous pipelines.
* Improve UI/UX for better accessibility.
* Enable offline translation support.
* Build APIs to integrate with government websites and mobile apps.





