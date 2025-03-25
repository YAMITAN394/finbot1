from google.cloud import firestore

def get_firestore_db():
    try:
        db = firestore.Client()
        return db
    except Exception as e:
        raise Exception(f"Failed to initialize Firestore client: {e}")