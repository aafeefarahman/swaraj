# upload_sample.py
import os
import csv
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = os.path.dirname(__file__)
KEY_PATH = os.path.join(BASE_DIR, "secrets", "serviceAccountKey.json")

cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()

COLLECTION = "translations"

with open(os.path.join(BASE_DIR, "corpus", "dataset_v1.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        doc_ref = db.collection(COLLECTION).document()
        doc_ref.set(row)

print("✅ Uploaded sample data to Firestore!")
