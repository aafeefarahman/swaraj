import firebase_admin
from firebase_admin import credentials, firestore

# Path to your downloaded JSON key file
cred = credentials.Certificate("./secrets/swarjya-translator-firebase-adminsdk-fbsvc-29f1b51369.json")

# Initialize the app only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_translation_to_firestore(source_text, translated_text, source_lang, target_lang):
    doc_ref = db.collection("translations").document()
    doc_ref.set({
        "source_text": source_text,
        "translated_text": translated_text,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "timestamp": firestore.SERVER_TIMESTAMP
    })
