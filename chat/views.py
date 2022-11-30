from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import *

def index(request):
    return render(request, 'index.html')

def register_user(request):
    return render(request, 'register.html')

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('chat:chat_app')
        else:
            messages.error(request, 'Invalid email and password')
            return redirect('chat:login_user')

    if request.user.is_authenticated:
        return redirect('chat:chat_app')
    else:
        return render(request,'login.html')


def chat(request):
    if request.user.is_authenticated:
        return render(request,'chat.html')
    else:
        print("non")

def chat_group(request):
    return render(request,'chat-group.html')

def send_msg(request):
    pass

