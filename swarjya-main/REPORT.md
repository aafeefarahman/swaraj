# REPORT.md
## Project: Swarjya — Gov Portal Translator
## Team:
- Shyam Cheni — shyamcheni (Coordinator, Frontend, Translation/TTS)
- Afeefa — Afeefa (Docs & DevOps)
- Deepthi — Deepthi_ch (Corpus Manager)
- Uday — Uday222 (Scraper Engineer)
- Sai Mohan — sai_mohan (Scraper & QA)

---

## 1. Project Overview
Swarjya is an open-source Streamlit application that translates formal English content found on government portals into local Indian languages. The app emphasizes accessibility (Text-to-Speech), corpus collection for Indic NLP, and offline-first considerations. The primary objective of the internship task is to build a "Corpus Collection Engine" that collects data while being useful to end users.

---

## 2. Problem Statement
A significant portion of government portal content is in formal English, which creates a comprehension barrier for many citizens. This app addresses that gap by enabling easy translation and audio playback, thus improving access to public information.

---

## 3. MVP & Features
**MVP (Week 1):**
- Streamlit UI for URL input, language selection, Translate button, and translated output display.
- Scraper that extracts readable text from government pages.
- Local translation pipeline (IndicTrans2 or API fallback).
- TTS playback for translated text.
- Corpus logger to collect original + translated pairs.

**Features:**
- URL scraping and content cleaning.
- Language selector (en → te/hi/bn/ta/ml/gu).
- TTS via `pyttsx3` or `gTTS`.
- Corpus export (CSV).

---

## 4. Architecture & Design
**High-level flow:**
