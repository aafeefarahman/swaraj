# translator.py
import requests

def translate(text, src="en", tgt="te"):
    url = "https://indictrans2-api.ai4bharat.org/translate"
    payload = {
        "input": [text],
        "src_lang": src,
        "tgt_lang": tgt,
        "model": "indictrans2"
    }
    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        return res.json()["output"][0]
    except Exception as e:
        return f"Error: {e}"
