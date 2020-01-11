from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .forms import RegisterForm, PasswordChange
from django import forms
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from post.models import Post
import logging


posts = Post.objects.all()
count = User.objects.count()
message = False


def index(request):
    posts = Post.objects.all()
    return render(request, 'allposts.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                posts = Post.objects.all()
                return render(request, 'allposts.html', {'posts': posts})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html')


def logout(request):
    count = User.objects.count()
    auth_logout(request)
    return redirect('post')


def change_passwd(request):
    if request.method == 'POST':
        form = PasswordChange(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('change_passwd')
    else:
        form = PasswordChange(request.user)
        return render(request, 'change_passwd.html', {'form': form})
