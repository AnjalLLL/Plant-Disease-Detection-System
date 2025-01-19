from django.core.management.base import BaseCommand
from myapp.db import get_db
from werkzeug.security import generate_password_hash

class Command(BaseCommand):
    help = "Create a static admin user in MongoDB"

    def handle(self, *args, **kwargs):
        # Check if the admin already exists in the database
        db = get_db()
        existing_admin = db.user.find_one({"role": "admin"})

        if existing_admin:
            self.stdout.write(self.style.SUCCESS("Admin already exists!"))
        else:
            # Static admin details
            admin_email = "admin@gmail.com"
            admin_password = "admin"  # Change this to a secure password
            hashed_password = generate_password_hash(admin_password)
            
            # Create a static admin user
            db.user.insert_one({
                "email": admin_email,
                "password": hashed_password,
                "role": "admin",
                "full_name": "Admin",
                
            })

            self.stdout.write(self.style.SUCCESS("Admin created successfully"))
