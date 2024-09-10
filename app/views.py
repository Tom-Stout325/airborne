from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import *
from .forms import *



def home(request):
    return render(request, 'app/home.html')

#=-=-=-=-=-=-=-=-=-=-=-=-=-> R E G I S T E R   V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


def loginView(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'form':form}

    return render(request, 'registration/login.html', context=context)



def logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")
