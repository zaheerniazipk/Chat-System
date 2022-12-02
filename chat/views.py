from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import *
from django.contrib.auth.models import User
import json

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
    if request.method == "POST":
        if 'add_friend' in request.POST:
            user_name=request.POST.get('user')
            friends_list(request,user_name)
    if request.user.is_authenticated:
        friendss_list = friend_list.objects.filter(from_user=request.user)
        return render(request,'chat.html', {'list': friendss_list})

    else:
        return redirect("chat:login_user")

def chat_group(request):
    if request.user.is_authenticated:

        friendss_list=friend_list.objects.filter(from_user=request.user)
        return render(request,'chat-group.html',{'list':friendss_list})
def send_id(request):
    body_unicode=request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)

def send_msg(request):
    pass

def user_logout(request):
    logout(request)
    return redirect('chat:login_user')

def friends_list(request,user_name):
    data=User.objects.filter(username=user_name)
    if data:
        too_user=data[0]
        froom_user=request.user
        if too_user.username==froom_user.username:
            print('you are trying to add your self')
        else:
            check_already_is_friend=friend_list.objects.filter(from_user=froom_user,to_user=too_user)
            if not check_already_is_friend:
                new_friend=friend_list(from_user=froom_user,to_user=too_user)
                new_friend.save()
                print("done")
            else:
                print("already friend")

