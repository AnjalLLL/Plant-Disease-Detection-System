from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from django.conf import settings
# Connect to MongoDB
def get_db():
    client = MongoClient('mongodb://localhost:27017')
    db = client['my_users']
    print("connected to mongodb")
    return db



        