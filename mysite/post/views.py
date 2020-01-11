from django.shortcuts import render, redirect
from .models import Post, Category
from django.http import HttpResponseRedirect
from django.contrib import messages

posts = Post.objects.all()


def post(request):
    posts = Post.objects.all()
    return render(request, "allposts.html", {"posts": posts})


def new_post(request):
    if request.method == 'POST':
        if request.POST['title'] != '' and request.POST['body'] != '':
            new_post = Post(
                post_title=request.POST['title'], post_body=request.POST['body'],
                user=request.user, category = Category.objects.get(id=request.POST['category']))
            new_post.save()
            messages.success(request, "SUCCESFULLY added")
            posts = Post.objects.all()
            return render(request, "allposts.html", {"posts": posts})
    else:
        categories = Category.objects.all()
        return render(request, "new_post.html", {"category": categories})


def myposts(request):
    id = request.user.id
    posts = Post.objects.filter(user_id=id)
    return render(request, "myposts.html", {"posts": posts})


def editpost(request, id):
    if request.method == 'POST':
        if request.POST['title'] != '' and request.POST['body'] != '':
            edit_post = Post.objects.get(id=id)
            edit_post.post_title = request.POST['title']
            edit_post.post_body = request.POST['body']
            edit_post.save()
            user_id = request.user.id
            posts = Post.objects.filter(user_id=user_id)
            return render(request, "myposts.html", {"posts": posts})
    else:
        post = Post.objects.get(id=id)
        return render(request, "editpost.html", {'post': post})


def deletepost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    user_id = request.user.id
    posts = Post.objects.filter(user_id=user_id)
    return render(request, "myposts.html", {"posts": posts})


def clickOnPost(request, id):
    selected_post = Post.objects.get(id=id)
    return render(request, "clickPost.html", {'post': selected_post})


# Categorie
# Design of website
#Likes or star
# Working hours and money
# Workers page(Find worker and information about worker and also CV)
# Apply for job and chat with Person
# Search for categorie
#Pagination  : MyModel.objects.all()[offset:limit]
