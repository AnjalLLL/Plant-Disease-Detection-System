from django.shortcuts import render, redirect
from django.contrib import messages
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db
from .predict import predict
import os
from django.conf import settings
import uuid
from django import forms
from .models import *
from django.shortcuts import render, redirect
from werkzeug.security import generate_password_hash,check_password_hash
from django.core.exceptions import ValidationError
from bson import ObjectId
from django.core.files.storage import FileSystemStorage

db = get_db()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Signup view
def signup(request):
    if request.method == "POST":
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")
        phone=request.POST.get("phone")
        gender = request.POST.get("gender")  # Capture gender
        location = request.POST.get("address")


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
            'phone':phone,
            'role': 'user',
            'gender':gender,
            'location':location,
        })
        
    
        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

# Login View


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Connect to MongoDB and verify the user
        db = get_db()
        user = db.user.find_one({"email": email})
        
        if user and check_password_hash(user["password"], password):  # Implement password hashing for production
            # Generate a token and set it in the cookies
            auth_token = str(uuid.uuid4())  # Generate a unique token for the session
            db.user.update_one({"email": email}, {"$set": {"auth_token": auth_token}})

            # Set the token in the cookie for future authentication
            response = redirect('test')  # Default redirection for regular users
            response.set_cookie('auth_token', auth_token)

            # Check if the user is an admin and redirect accordingly
            if user.get('role') == 'admin':
                response = redirect('admin')  # Redirect to admin panel if user is admin
                response.set_cookie('auth_token', auth_token)
                
            return response
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")  # Adjust this to your login template
    else:
        return render(request, "login.html")



#Logout View
def logout(request):
    # Clear the auth_token from the cookies
    response = redirect('login')  # Redirect to the login page after logout
    response.delete_cookie('auth_token')  # Remove token from cookies

    messages.success(request, "Logged out successfully!")
    return response



ALLOWED_IMAGE_FORMATS=['.jpg','.jpeg','.png']
# Handle uploaded files
def handle_uploaded_file(f):
    file_extension=os.path.splitext(f.name)[1].lower()
    if file_extension not in ALLOWED_IMAGE_FORMATS:
        raise ValidationError(f"Unsupported file format.Please upload an image in {','.join(ALLOWED_IMAGE_FORMATS)} format.")
    #save the file if its a valid format
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
    
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

#Test View
def test(request):
    is_authenticated = request.COOKIES.get('auth_token') is not None
    error =None
    if request.method == "POST":
        if "image" in request.FILES:
            uploaded_image = request.FILES["image"]

            try:
                file_path = handle_uploaded_file(uploaded_image)  # Save the uploaded image

            # Make a prediction using the image
                predicted_class = predict(file_path)

            # Fetch disease info based on predicted class
              
                if predicted_class.lower() == "healthy":
                    # Fetch information for healthy plants
                    disease_info = db["disease_data"].find_one({"disease_name": "Healthy"})
                else:
                    # Fetch disease info based on the predicted class
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
               

                return render(request, "test.html", {
                
                "predicted_class": predicted_class,
                "partial_info": partial_info,
                "full_info": full_info if is_authenticated else None,
                "is_authenticated": is_authenticated,
                "error":error,
            })
            except ValidationError as e:
                # Handle validation error for invalid file format
                error = e.message if isinstance(e.message, str) else e.message[0]
                return render(request, "test.html", {"error": error, "is_authenticated": is_authenticated})
            
            except Exception as e:
                # Handle any other unexpected errors
                error = f"An unexpected error occurred: {str(e)}"
                return render(request, "test.html", {"error": error, "is_authenticated": is_authenticated})

    # Default render for GET requests
    return render(request, "test.html", {"is_authenticated": False})

def home(request):
    plant_data = db.plant_info

    # Fetch all plant data
    plants = plant_data.find()

    # Pass the plant data to the template
    return render(request, 'home.html', {'plants': plants})






# Admin Dashboard




# Admin Dashboard


from .forms import ProfileUpdateForm

# View to display the user's profile
def profile(request):
    if not request.mongo_user:
        # Handle case where user is not authenticated
        return redirect('login')

    db = get_db()

    # Fetch the user data from the user collection
    user_data = db.user.find_one({"_id": ObjectId(request.mongo_user['_id'])})

    # Fetch additional user details like full_name, gender, location, etc.
    if user_data:
        full_name = user_data.get("full_name", "")
        email = user_data.get("email", "")
        phone = user_data.get("phone", "")
        gender = user_data.get("gender", "")  # Assuming the field is 'gender'
        location = user_data.get("location", "")  # Assuming the field is 'location'
    else:
        full_name = email = phone = gender = location = ""

    # Fetch any profile details from the profile_details collection
    profile_data = db.profile_details.find_one({"user_id": ObjectId(request.mongo_user['_id'])})

    return render(request, 'profile.html', {
        'user_data': user_data,
        'profile_data': profile_data,
        'full_name': full_name,
        'email': email,
        'phone': phone,
        'gender': gender,
        'location': location
    })

# View to update the user's profile
# views.py
from gridfs import GridFS
from django.core.files.storage import default_storage
from bson import ObjectId
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import ProfileUpdateForm

def update_profile(request):
    if not request.mongo_user:
        return redirect('login')

    db = get_db()
    fs = GridFS(db)  # Initialize GridFS
    user_data = db.user.find_one({"_id": request.mongo_user['_id']})
    profile_data = db.profile_details.find_one({"user_id": request.mongo_user['_id']})

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            updated_data = form.cleaned_data
            
            # If a profile picture is uploaded, save it to GridFS
            if 'profile_picture' in request.FILES:
                profile_picture = request.FILES['profile_picture']
                file_id = fs.put(profile_picture)  # Store file in GridFS
                updated_data['profile_picture'] = file_id  # Store file_id in the database

            # Store or update profile data
            if profile_data:
                db.profile_details.update_one(
                    {"user_id": request.mongo_user['_id']},
                    {"$set": updated_data}
                )
            else:
                updated_data['user_id'] = request.mongo_user['_id']
                db.profile_details.insert_one(updated_data)

            return redirect('user_profile')
    else:
        initial_data = {
            'bio': profile_data.get('bio', '') if profile_data else '',
            'profile_picture': profile_data.get('profile_picture', '') if profile_data else ''
        }
        form = ProfileUpdateForm(initial=initial_data)

    return render(request, 'update_profile.html', {'form': form, 'user_data': user_data})

from django.http import HttpResponse
from gridfs import GridFS
from django.shortcuts import get_object_or_404

def view_image(request, file_id):
    db = get_db()
    fs = GridFS(db)

    # Retrieve the image by its file_id
    file = fs.get(ObjectId(file_id))  # Use ObjectId to fetch the file from GridFS
    response = HttpResponse(file.read(), content_type='image/jpeg')
    response['Content-Disposition'] = f'inline; filename="{file.filename}"'
    return response
