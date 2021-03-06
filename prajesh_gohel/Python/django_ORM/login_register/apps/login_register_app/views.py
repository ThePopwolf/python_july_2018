from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False

    return render(request, 'login_register/index.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')

        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['email'] = request.POST['email']
            request.session['logged_in'] = True
            return redirect('/success')

    return redirect('/')

def verify(request):
    errors = User.objects.login_validator(request.POST)
    try:
        user = User.objects.get(email=request.POST['email'])

    except:
        messages.error(request, "Login Failed")
        return redirect('/')

    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')

        elif not bcrypt.checkpw(request.POST['passlog'].encode(), user[0].password.encode()):
            messages.error(request, "Login failed")
            return redirect('/')

        else:
            request.session['email'] = request.POST['email']
            request.session['logged_in'] = True
            return redirect('/success')

def success(request):
    if 'first_name' not in request.session:
        return redirect('/')

    return render(request, 'login_register/success.html')

def log_out(request):
    del request.session['email']
    request.session['logged_in'] = False
    return redirect('/')
