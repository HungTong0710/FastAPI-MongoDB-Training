from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "training"
COLLECTION = "stories"

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = client[COLLECTION]
    print("Connected to DB!")
except Exception as e:
    print(f"detail error: {e}")