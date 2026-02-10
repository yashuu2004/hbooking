from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "register.html", {
                "error": "Email and password are required"
            })

        email = email.strip().lower()  # ✅ no caps issues

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'].strip().lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/trips/')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
