from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        if password != cpassword:
            messages.error(request, "Passwords do not match. Please retry.")
            return redirect("/signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("/signup")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("/signup")
        
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()       
        return redirect("/login")
    
    else:
        messages.info(request, "Please sign up.")
        
    return render(request, "signup.html")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        myuser = authenticate(username=username, password=password)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'Login Successfully')
            return HttpResponse("Login Successful")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
        
    return render(request, "login.html")


