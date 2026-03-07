import os
import csv
import json
import datetime

# path to your service account key
BASE_DIR = os.path.dirname(__file__)
KEY_PATH = os.path.join(BASE_DIR, "secrets", "serviceAccountKey.json")

USE_FIREBASE = os.path.exists(KEY_PATH)

if not USE_FIREBASE:
    print("⚠ Firebase service account not found at:", KEY_PATH)
    print("Please create secrets/serviceAccountKey.json or set USE_FIREBASE=True with correct path.")
    # Optionally exit or write an empty CSV:
    # exit(1)

if USE_FIREBASE:
    import firebase_admin
    from firebase_admin import credentials, firestore

    cred = credentials.Certificate(KEY_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # collection name (adjust if your app uses a different collection name)
    COLLECTION = "translations"

    docs = db.collection(COLLECTION).stream()

    os.makedirs(os.path.join(BASE_DIR, "corpus"), exist_ok=True)
    csv_path = os.path.join(BASE_DIR, "corpus", "firebase_translations.csv")
    jsonl_path = os.path.join(BASE_DIR, "corpus", "firebase_translations.jsonl")

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile, \
         open(jsonl_path, "w", encoding="utf-8") as jsonlfile:
        writer = csv.writer(csvfile)
        # header: adjust according to the fields you store
        headers = ["doc_id", "url", "title", "source_text", "translated_text", "source_lang", "target_lang", "user", "created_at"]
        writer.writerow(headers)

        count = 0
        for doc in docs:
            data = doc.to_dict()
            doc_id = doc.id
            url = data.get("url", "")
            title = data.get("title", "") or data.get("source_title", "")
            source_text = data.get("source_text", "") or data.get("english", "")
            translated_text = data.get("translated_text", "") or data.get("translation", "")
            source_lang = data.get("source_lang", "") or data.get("src_lang", "")
            target_lang = data.get("target_lang", "") or data.get("tgt_lang", "")
            user = data.get("user", "") or data.get("created_by", "")
            created_at = data.get("created_at", "")
            # convert timestamps if needed
            if hasattr(created_at, "isoformat"):
                created_at = created_at.isoformat()

            writer.writerow([doc_id, url, title, source_text, translated_text, source_lang, target_lang, user, created_at])
            jsonlfile.write(json.dumps({"doc_id":doc_id, **data}, ensure_ascii=False) + "\n")
            count += 1

    print(f"✅ Exported {count} documents to:")
    print("  -", csv_path)
    print("  -", jsonl_path)
else:
    # If you want a local fallback to read a local jsonl file (e.g., data/local_translations.jsonl)
    SAMPLE_LOCAL = os.path.join(BASE_DIR, "data", "local_translations.jsonl")
    if os.path.exists(SAMPLE_LOCAL):
        print("Using local fallback file:", SAMPLE_LOCAL)
        os.makedirs(os.path.join(BASE_DIR, "corpus"), exist_ok=True)
        csv_path = os.path.join(BASE_DIR, "corpus", "firebase_translations.csv")
        with open(SAMPLE_LOCAL, "r", encoding="utf-8") as f_in, open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["source_text","translated_text","target_lang","url","created_at"])
            count = 0
            for line in f_in:
                item = json.loads(line)
                writer.writerow([
                    item.get("source_text",""),
                    item.get("translated_text",""),
                    item.get("target_lang",""),
                    item.get("url",""),
                    item.get("created_at","")
                ])
                count += 1
        print(f"✅ Created {csv_path} from local fallback ({count} rows)")
    else:
        print("No Firebase key and no local fallback found. Please provide one.")
