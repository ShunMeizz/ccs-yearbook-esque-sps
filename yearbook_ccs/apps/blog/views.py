from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Blog, Comment

from .forms import BlogForm, CommentForm

@login_required
def blog_home(request):
    posts = get_post()
    action = request.POST.get('action')
    print("blog post")
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if action == 'create':
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user_id = request.user.id
                blog.save()
                return redirect("intermediary")
        if action == "edit":
            post_id = request.POST.get('post_id')
            blogpost = get_object_or_404(Blog, id=post_id)

            title = request.POST.get('title')
            content = request.POST.get('content')
            print("edit")

            blogpost.title = title
            blogpost.content = content
            if request.FILES.get('media'):
                blogpost.media = request.FILES['media']  

            blogpost.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if action == "report":
            post_id = request.POST.get('post_id')
            blogpost = get_object_or_404(Blog, id=post_id)

            print("report")
    else:
        form = BlogForm() 
    return render(request,"blog/blog_home.html", {'form':form,'posts':posts})

def comment_section(request):
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = 10
            comment.user_id = request.user.id

# TEMP TO SHOW ALL BLOGS WITHOUT FILTER FROM ISAPPROVED. 
# TO BE DELETED AFTER ISAPPROVED FILTERS ARE WORKING AND DONE
def get_post():
    return Blog.objects.all().order_by("-date")

def intermediary(request):
    return render(request, "blog/test.html")

def pending_post(request):
    user = request.user.username
    pending = Blog.objects.filter(user=request.user).order_by("-date")
    action = request.POST.get('action')

    if request.method == "POST":
        if action == "edit":
            print("my posts")
            post_id = request.POST.get('post_id')
            blogpost = get_object_or_404(Blog, id=post_id)

            title = request.POST.get('title')
            content = request.POST.get('content')

            blogpost.title = title
            blogpost.content = content
            if request.FILES.get('media'):
                blogpost.media = request.FILES['media']  # Update media if a new file is uploaded

            blogpost.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request,"blog/blog_pending.html",{'pending':pending,'user':user})
    else:
        return render(request,"blog/blog_pending.html",{'pending':pending,'user':user})

def view_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'blog/components/baseblog_post.html', {'post': post})

def delete_post(request, user_id):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')
        post = get_object_or_404(Blog, id=post_id)

        if action == "delete":
            post.delete()
    return redirect('blog_home')
