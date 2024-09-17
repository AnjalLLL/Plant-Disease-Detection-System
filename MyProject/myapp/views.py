from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def signup(request):
    # if request.method == "POST":
    #   uname = request.POST.get("uname")
    #   full_name = request.POST.get("name")
    #   email = request.POST.get("email")
    #   gender = request.POST.get("Gender")
    #   address = request.POST.get("address")
    #   phone = request.POST.get("phone")
    #   pass1 = request.POST.get("password1")
    #   password = request.POST.get("password2")

    #   if pass1 == password:
     
    #    new_user = CustomUser(username=uname,full_name=full_name,email=email,gender=gender,address=address,phone=phone,password=password)
    #    new_user.save()
      
    #    return redirect("dashboard")
    #   else:
    #     raise forms.ValidationError("Passwords don't match")
    # else:
     return render(request,'signup.html')

 

def signin(request):
    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     password = request.POST.get("Password")
    #     print(email,password)
    #     try:
    #         user_details = CustomUser.objects.get(email=email)
    #         if (password, user_details.password):
    #             # Authentication successful
    #             # Access user_details fields here
    #             request.session['user_id'] = user_details.id  # Store user_id in session
    #             return redirect('dashboard')
                
    #         else:
    #             # Password incorrect
    #             return render(request, 'sign-in.html', {'error_message': 'Invalid password'})
    #     except CustomUser.DoesNotExist:
    #         # User with given username does not exist
    #         return render(request, 'sign-in.html', {'error_message': 'User does not exist'})
    # else:
        return render(request, 'sign-in.html')

# def termsandcondition(request):
#   return render(request,"termsandcondition.html")

def about(request):
  return render(request,"about.html")

# def logout_view(request):
#     user = get_logged_in_user(request)
#     if user in request.session:
#         del request.session['user']
#     return redirect('signin')

def test(request):
     return render(request,"test.html")