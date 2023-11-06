import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 初始化Firebase服務
def initialize_firebase():
    try:
        cred = credentials.Certificate("myproject01-be1b7-firebase-adminsdk-1mh85-d166ea266f.json")
        firebase_admin.initialize_app(cred)
        print("Firebase Initialized")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

# 保存數據到Firebase
def save_data_to_firebase(collection_name, data):
    try:
        db = firestore.client()
        db.collection(collection_name).add(data)
        print(f"Data added to {collection_name} collection")
    except Exception as e:
        print(f"Error adding data to {collection_name} collection: {e}")

# 請確保在程序開始時調用 initialize_firebase 函數
# initialize_firebase()

# 舉例來說，你可以這樣調用 save_data_to_firebase 函數
# save_data_to_firebase('news_titles', {'title': 'New Article'})
