from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog

from .forms import BlogForm

@login_required
def blog_home(request):
    posts = get_post()
    user = request.user
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user_id = request.user.id
            blog.save()
            print()
            # return render(request,"blog/blog_home.html", {'form':form,'blog':blog,'posts':posts})
            return redirect("intermediary")
    else:
        form = BlogForm() 
    return render(request,"blog/blog_home.html", {'form':form,'posts':posts,'user':user})

def get_post():
    return Blog.objects.all()

def intermediary(request):
    return render(request, "blog/test.html")

def pending_post(request):
    pending = Blog.objects.filter(isApproved=-1)
    return render(request,"blog/blog_pending.html",{'pending':pending})

def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Blog,id=post_id)
        post.delete()
    return redirect('blog_home')
