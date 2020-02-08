from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from post.models import Post

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
                coming_page=request.GET['next']
                return redirect(coming_page)
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')

