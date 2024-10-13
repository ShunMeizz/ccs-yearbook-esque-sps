from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog

from .forms import BlogForm

@login_required
def blog_home(request):
    posts = get_post()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user_id = request.user.id
            blog.save()
            return render(request,"blog/blog_home.html", {'form':form,'blog':blog,'posts':posts})
    else:
        form = BlogForm() 
    return render(request,"blog/blog_home.html", {'form':form,'posts':posts})

def get_post():
    return Blog.objects.all()

def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Blog,id=post_id)
        post.delete()
    return redirect('blog_home')
