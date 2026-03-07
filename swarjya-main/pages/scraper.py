import streamlit as st
import os
import sqlite3
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# ---------- FUNCTIONS ----------

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def scrape_and_clean(url, retries=2):
    attempt = 0
    while attempt <= retries:
        driver = None
        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.set_page_load_timeout(15)
            driver.get(url)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "p"))
                )
            except TimeoutException:
                st.warning(f"⚠️ Timeout waiting for content on {url}")

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
                tag.decompose()

            if "Access Denied" in soup.get_text() or "Forbidden" in soup.get_text():
                st.error(f"🚫 Access denied for {url}")
                return None

            title = soup.title.string.strip() if soup.title else "No Title Found"

            paragraphs = []
            for p in soup.find_all('p'):
                text = p.get_text(strip=True)
                if text:
                    paragraphs.extend(chunk_text(text, 500))

            if not paragraphs:
                st.warning(f"⚠️ No readable content found for {url}")
                return None

            return {"url": url, "title": title, "content": paragraphs}

        except Exception as e:
            st.error(f"❌ Attempt {attempt+1} failed for {url}: {e}")
            attempt += 1
            time.sleep(2)
        finally:
            if driver:
                driver.quit()

    return None

def save_to_file(data):
    os.makedirs("scraped_data", exist_ok=True)
    count = len(os.listdir("scraped_data")) + 1
    filename = f"scraped_data/sample{count}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"URL: {data['url']}\n")
        f.write(f"Title: {data['title']}\n\n")
        for para in data['content']:
            f.write(para + "\n\n")

    st.success(f"✅ Saved {len(data['content'])} paragraph(s) to {filename}")

def save_to_db(data):
    conn = sqlite3.connect("scraped_data_test.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scraped_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            title TEXT,
            paragraph TEXT
        )
    ''')
    for para in data['content']:
        c.execute('INSERT INTO scraped_content (url, title, paragraph) VALUES (?, ?, ?)',
                  (data['url'], data['title'], para))
    conn.commit()
    conn.close()
    st.success(f"💾 Saved {len(data['content'])} paragraph(s) to database")

# ---------- STREAMLIT APP ----------

st.set_page_config(page_title="Web Scraper", layout="centered")
st.title("🌐 Web Scraper & Saver")
st.subheader("Scrape paragraphs from URLs and save to file + DB")

urls_input = st.text_area("Enter URLs (separate multiple URLs by space)")
chunk_size = st.number_input("Chunk size for paragraphs", min_value=100, max_value=2000, value=500)

if st.button("🚀 Scrape & Save"):
    if not urls_input.strip():
        st.warning("⚠️ Please enter at least one URL.")
    else:
        urls = urls_input.split()
        for url in urls:
            st.info(f"🔍 Scraping: {url}")
            data = scrape_and_clean(url)
            if data:
                save_to_file(data)
                save_to_db(data)
