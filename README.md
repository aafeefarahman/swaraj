# swaraj
Swaraj is a cloud-native web app empowering every Indian citizen with equal access to digital governance. It auto-translates government portals into 22 scheduled languages, enables real-time TTS/SST in local accents, and delivers a seamless, intuitive multilingual experience for all—no prior training needed.

🎯 Day 1 Task
*Front end dev* 
✅ Finalize basic UI structure in Streamlit (textbox, dropdowns, buttons)
✅ Setup folder structure✅ Add dummy URL input + translate button (connect later)
✅ Help unblock anyone stuck

 *2.Translation & TTS/STT*
explore tts, stt apis .

*3 Corpus & Dataset Manager* 	
✅ Create a folder data/<✅ Add a .csv file structure like src_lang, tgt_lang, source_text, translated_text
✅ Learn how to append translation data to it from UI.

 4.*Web Scraping Engineer* 
✅ Build working scraper.py that accepts a gov URL and returns clean paragraph text<b✅ Test on 2-3 real gov.in pages
✅ Handle invalid URLs gracefully


 *5.Docs & DevOps* 
✅ Write initial README.md: project intro + team roles
✅ List tech stack
✅ Create GitLab wiki page  to track daily progress
✅ Try running the project locally and note any setup issues


📅 *Day 2 Taskboard – Swarajya: AI-Powered Government Portal Translator*  
** *Coordinator + Frontend Developer + TTS/Translation* **
[x] Push base code to GitHub (already done)
[ ] Build basic Streamlit UI:
Input field for URL
Language selection dropdowns (Source, Target)
"Translate" button (initially non-functional)
[ ] Add dummy TTS (Text-to-Speech) using pyttsx3 or placeholder audio
[ ] Review each member's setup individually
---
🧠  *(Scraping Engineer)* 
[ ] Learn to scrape basic government web pages (use https://www.india.gov.in)
[ ] Write script using requests + BeautifulSoup to extract only readable paragraph content
[ ] Save sample scraped data to scraped_data/sample1.txt
---
📖  *(Corpus & Dataset Manager)* 
[ ] Create structure to store translation pairs
Format: { "en": "Hello", "te": "హలో" }
[ ] Store at least 3 hardcoded translation examples in data/corpus.csv
[ ] Pick 2–3 government websites to use as sample inputs
---
📑  ( *Documentation & DevOps)* 
[ ] Update README.md with:
✅ Project title
✅ Vision & Description
✅ Team member roles
✅ Tech stack (table)
[ ] Create docs/setup.md with:
[ ]Instructions to install
VS Code, Python 3.11+, uv, and packages
Screenshot examples
[ ]Write notes on sprint meeting while user reporting there work 
[name ,Task ,✅finished ,❌Pending ]
[ ] Make sure project folder follows:
/swarajya
├── app.py
├── translator.py
├── tts.py
├── data/
│   └── corpus.csv
├── docs/
│   └── setup.md
└── README.md
