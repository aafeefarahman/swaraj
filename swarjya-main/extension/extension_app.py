from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    target_lang = data.get("target_lang", "te")
    
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return jsonify({"translated": translated})
    except Exception as e:
        return jsonify({"translated": text, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
