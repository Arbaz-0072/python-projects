from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login as auth_login

def index(request):
    from django.contrib.auth.decorators import login_required
    return render(request, 'index.html')

def loginuser(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
