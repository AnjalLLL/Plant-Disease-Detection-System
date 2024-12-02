from django.shortcuts import render, redirect
from django.contrib import messages
from werkzeug.security import generate_password_hash, check_password_hash
from django.urls import reverse
from .db import get_db
from .predict import predict
import os
from django.conf import settings
import uuid
db = get_db()  # MongoDB connection setup

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

# Signup view
def signup(request):
    if request.method == "POST":
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Check if email exists
        if db.user.find_one({'email': email}):
            messages.error(request, "Email already exists!")
            return render(request, 'signup.html')

        # Insert user data into MongoDB
        db.user.insert_one({
            'full_name': full_name,
            'email': email,
            'password': hashed_password,
        })

        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


# Login View
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Query MongoDB for user
        user = db.user.find_one({"email": email})
        if user and check_password_hash(user["password"], password):
            # Generate a unique token
            token = str(uuid.uuid4())

            # Save the token in the database
            db.user.update_one({"email": email}, {"$set": {"auth_token": token}})

            # Set the token in a cookie
            response = redirect('test')
            response.set_cookie('auth_token', token, httponly=True)

            messages.success(request, "Login successful!")
            return response
        else:
            messages.error(request, "Invalid email or password!")
            return render(request, "login.html")

    return render(request, "login.html")
def logout(request):
    # Clear the auth_token from the cookies
    response = redirect('login')  # Redirect to the login page after logout
    response.delete_cookie('auth_token')  # Remove token from cookies

    messages.success(request, "Logged out successfully!")
    return response


# Handle uploaded files


# Test view (Disease prediction)
# Test view (Disease prediction)
# Test view (Disease prediction)
# Test view (Disease prediction)
