from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def thaistory(req):
	return render(req, 'myweb/thaistory.html')

def International(req):
	return render(req, 'myweb/International.html')

def Login(req):
    return render(req, 'myweb/Login.html')

def Register(req):
    return render(req, 'myweb/Register.html')

def indexuser(req):
    return render(req, 'myweb/indexuser.html')

def thaistoryuser(req):
	return render(req, 'myweb/thaistoryuser.html')

def Internationaluser(req):
	return render(req, 'myweb/Internationaluser.html')

def requeststory(req):
    Destinations = Destination.objects.all()
    return render(req, 'myweb/requeststory.html', {'Destinations': Destinations})

def Register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f"New account created: {username}")
            login(req, user)
            return redirect("/")

        else:
            for msg in form.error_messages:
                messages.error(req, f"{msg}: {form.error_messages[msg]}")

            return render(req,
                          template_name = "myweb/Register.html",
                          context={"form":form})
    form = UserCreationForm(req.POST)
    return render(req,
                template_name = "myweb/Register.html",
                context={"form":form})

def Login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.info(req, f"You are now logged in as {username}")
                return redirect('/indexuser')
            else:
                messages.error(req, "Invalid username or password.")
        else:
            messages.error(req, "Invalid username or password.")
    form = AuthenticationForm()
    return render(req,
                  template_name = "myweb/Login.html",
                  context={"form":form})

def logout(req):
    logout(req)
    messages.info(req, "Logged out successfully!")
    return redirect("/indexuser")