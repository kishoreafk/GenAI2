from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from myproject.forms import UserRegistrationForm  # If forms.py is inside myproject


# User Registration View
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    
    return render(request, "register.html", {"form": form})

# User Login View
def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")  # Redirect logged-in users
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "login.html")

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("login")

@login_required
def dashboard(request):
    return render(request, "dashboard.html", {"user": request.user})
@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

@login_required
def judge_dashboard(request):
    return render(request, "judge_dashboard.html")

@login_required
def participant_dashboard(request):
    return render(request, "participant_dashboard.html")
