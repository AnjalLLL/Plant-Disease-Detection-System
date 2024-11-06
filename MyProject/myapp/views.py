from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from werkzeug.security import generate_password_hash,check_password_hash
from .db import get_db



def home(request):
    return render(request, 'home.html')

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

def about(request):
  return render(request,"about.html")

# def logout_view(request):
#     user = get_logged_in_user(request)
#     if user in request.session:
#         del request.session['user']
#     return redirect('signin')

def test(request):
     return render(request,"test.html")