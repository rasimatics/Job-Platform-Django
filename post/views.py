from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Post, Category
from django.contrib.auth.decorators import login_required


def post(request):
    posts = Post.objects.all()
    return render(request, "posts/allposts.html", {"posts": posts})


@login_required(login_url='/login/')
def new_post(request):
    if request.method == 'POST':
        if request.POST['title'] != '' and request.POST['body'] != '':
            new_post = Post(
                post_title=request.POST['title'], post_body=request.POST['body'],
                user=request.user, category=Category.objects.get(id=request.POST['category']),
                price=request.POST['price'])
            new_post.save()
            return redirect('post')
    else:
        categories = Category.objects.all()
        return render(request, "posts/new_post.html", {"category": categories})


@login_required(login_url='/login/')
def myposts(request):
    user_id = request.user.id
    posts = Post.objects.filter(user_id=user_id)
    return render(request, "posts/myposts.html", {"posts": posts})


@login_required(login_url='/login/')
def editpost(request, slug):
    if request.method == 'POST':
        if request.POST['title'] != '' and request.POST['body'] != '':
            edit_post = Post.objects.get(slug=slug)
            edit_post.post_title = request.POST['title']
            edit_post.post_body = request.POST['body']
            edit_post.save()
            user_id = request.user.id
            posts = Post.objects.filter(user_id=user_id)
            return render(request, "posts/myposts.html", {"posts": posts})
    else:
        post = Post.objects.get(slug=slug)
        if (post.user == request.user):
            return render(request, "posts/editpost.html", {'post': post})
        else:
            return HttpResponse("<h2>You cannot edit this post!")


@login_required(login_url='/login/')
def deletepost(request, slug):
    post = Post.objects.get(slug=slug)
    if (post.user == request.user):
        post.delete()
        user_id = request.user.id
        posts = Post.objects.filter(user_id=user_id)
        return render(request, "posts/myposts.html", {"posts": posts})
    else:
        return HttpResponse("<h2>You can't delete this post")


def clickOnPost(request, slug):
    try:
        selected_post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        selected_post = None
    return render(request, "posts/postDetail.html", {'post': selected_post})

class SearchResultsView(ListView):
    model = Post
    template_name = 'posts/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(post_title__contains=query) |
            Q(post_body__icontains=query) |
            Q(category__category__icontains=query)
        )
        return object_list