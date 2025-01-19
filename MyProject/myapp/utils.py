from werkzeug.security import generate_password_hash
from .db import get_db

def create_admin():
    """
    Creates an admin user in the MongoDB database if one doesn't already exist.
    """
    db = get_db()
    admin_email = "admin@gmail.com"  # Replace with your desired admin email

    # Check if an admin user already exists
    existing_admin = db.user.find_one({"email": admin_email, "role": "admin"})
    if not existing_admin:
        db.user.insert_one({
            "full_name": "Super Admin",  # Replace with a suitable name
            "email": admin_email,
            "password": generate_password_hash("admin@123"),  # Replace with a strong password
            "role": "admin"
        })
        print("Admin user created successfully!")
    else:
        print("Admin user already exists.")
