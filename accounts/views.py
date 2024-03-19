from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'this username already taken')
                return redirect('accounts/register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'this username already taken')
                    return redirect('accounts/register', 'email is already taken')
                else:
                    # Looks Good
                    user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('/index')
                    user.save()
                    messages.success(request, 'You are now registered and can login now')
                    return redirect('/login')

        else:
            messages.error(request, 'Passwords does not match')
            return redirect('accounts/register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login User login
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now loggedIn successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')