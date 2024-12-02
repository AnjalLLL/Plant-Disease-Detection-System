from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib import messages
from werkzeug.security import generate_password_hash, check_password_hash
from django.urls import reverse
from .db import get_db
from .predict import predict
import os
from django.conf import settings
import uuid
db = get_db()  # MongoDB connection setup
=======
from django.contrib.auth import authenticate, login
from django import forms
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from werkzeug.security import generate_password_hash,check_password_hash
from .db import get_db


>>>>>>> d3ad71db99d5001a4a13950c648f52cae6206c59

def home(request):
    return render(request, 'home.html')

<<<<<<< HEAD
=======
def signup(request):
    if request.method == "POST":
      #  uname = request.POST.get("uname")
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("Gender")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")
        #Hash the password before storing it
        
        if password != confirm_password:
            messages.error(request,"Passwords do not match!", "error")
            return render(request, 'about.html')

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        db = get_db()

        # Check if the email already exists
        if db.users.find_one({'email': email}):
            messages.error(request,"Email already exists!")
            return render(request, 'base.html')

        # Insert user into the users collection
        db.users.insert_one({
            'full_name': full_name,
            'password': hashed_password,
            'email': email,
            'phone': phone,
            'address': address,
            'gender': gender,
        })

        messages.success(request,"Signup successful! Please log in.")
        return redirect('about')

    return render(request, 'home.html')

def signin(request):
    db = get_db()  # Get the database connection
    users_collection = db["users"]
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Find the user by email
        user = db.users.find_one({'email': email})

        # Check if user exists and password is correct
        if user and check_password_hash(user['password'], password):
            # Successful login logic here (e.g., set session)
            #request.session['user_id'] = user['_id']  # Storing user ID in session
            return redirect('home')  # Redirect to home page after successful login
        else:
            # If invalid credentials, render the login page with an error
            messages.error(request, "Invalid email or password")
            return render(request, 'about.html')

    return render(request, 'base.html')

>>>>>>> d3ad71db99d5001a4a13950c648f52cae6206c59
def about(request):
    return render(request, "about.html")

# Signup view
def signup(request):
    if request.method == "POST":
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

<<<<<<< HEAD
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
=======
def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def test(request):
    def test(request):
    if request.method == "POST":
        if "image" in request.FILES:
            uploaded_image = request.FILES["image"]
            file_path = handle_uploaded_file(uploaded_image)  # Save the uploaded image

            # Make a prediction using the image
            predicted_class = predict(file_path)

            # Fetch disease info based on predicted class
            disease_info = db["disease_data"].find_one({"disease_name": predicted_class})
            
            # If no information is found, handle gracefully
            if not disease_info:
                partial_info = "No information available for this disease."
                full_info = None
            else:
                # Prepare partial and full information
                partial_info = {
                    "disease_name": disease_info.get("disease_name", "Unknown disease"),
                    "description": disease_info.get("description", "Description not available."),
                }

                full_info = {
                    "disease_name": disease_info.get("disease_name", "Unknown disease"),
                    "description": disease_info.get("description", "Description not available."),
                    "prevention": disease_info.get("prevention", "Prevention information not available."),
                    "treatment": disease_info.get("treatment", "Treatment information not available."),
                }

            # Check if the user is authenticated
            is_authenticated = request.COOKIES.get('auth_token') is not None

            return render(request, "test.html", {
                "predicted_class": predicted_class,
                "partial_info": partial_info,
                "full_info": full_info if is_authenticated else None,
                "is_authenticated": is_authenticated,
            })

    # Default render for GET requests
    return render(request, "test.html", {"is_authenticated": False})
>>>>>>> d3ad71db99d5001a4a13950c648f52cae6206c59
