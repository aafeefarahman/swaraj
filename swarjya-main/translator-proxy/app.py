import re, requests
from flask import Flask, request, Response, render_template_string
from bs4 import BeautifulSoup, NavigableString, Comment
from deep_translator import GoogleTranslator

app = Flask(__name__)
SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

# -------- Translation logic --------
def translate_dom_keep_layout(html, base_url, target_lang):
    soup = BeautifulSoup(html, "html.parser")

    # Translate only visible text nodes
    for el in soup.find_all(string=True):
        if isinstance(el, Comment):  # skip comments
            continue
        text = el.strip()
        if text and len(text.split()) > 0:
            try:
                translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
                el.replace_with(translated)
            except Exception:
                pass

    # Make relative URLs absolute so links/forms work
    for tag in soup.find_all(["a", "link", "script", "img", "form"]):
        attr = "href" if tag.name in ["a", "link"] else "src" if tag.name in ["script", "img"] else "action"
        if tag.has_attr(attr):
            if not tag[attr].startswith(("http", "https", "mailto", "#")):
                tag[attr] = requests.compat.urljoin(base_url, tag[attr])

    return str(soup)

# -------- Routes --------
@app.route("/")
def home():
    return render_template_string("""
    <h2>🌐 Translation Proxy</h2>
    <form action="/t/hi">
      <input type="text" name="url" placeholder="https://services.india.gov.in/" size="50" required>
      <select name="lang" onchange="this.form.action='/t/'+this.value">
        <option value="hi">हिन्दी</option>
        <option value="te">తెలుగు</option>
        <option value="ta">தமிழ்</option>
        <option value="kn">ಕನ್ನಡ</option>
        <option value="ml">മലയാളം</option>
        <option value="en">English</option>
      </select>
      <button type="submit">Translate</button>
    </form>
    """)

@app.route("/t/<lang>")
def translate_route(lang):
    url = request.args.get("url")
    if not url:
        return "Missing ?url=", 400

    # fetch the page
    r = SESSION.get(url)
    ctype = r.headers.get("Content-Type", "text/html")

    if "html" not in ctype.lower():
        return Response(r.content, content_type=ctype)

    # translate and re-render
    translated_html = translate_dom_keep_layout(r.text, r.url, lang)
    return Response(translated_html, content_type="text/html")

if __name__ == "__main__":
    app.run(debug=True)
