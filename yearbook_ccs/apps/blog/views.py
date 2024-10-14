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
            # return render(request,"blog/blog_home.html", {'form':form,'blog':blog,'posts':posts})
            return redirect("intermediary")
    else:
        form = BlogForm() 
    return render(request,"blog/blog_home.html", {'form':form,'posts':posts})

# TEMP TO SHOW ALL BLOGS WITHOUT FILTER FROM ISAPPROVED. 
# TO BE DELETED AFTER ISAPPROVED FILTERS ARE WORKING AND DONE
def get_post():
    return Blog.objects.all().order_by("-date")

# TO USE FOR BLOGPAGE
# def approved_post(request):
#     approved = Blog.objects.filter(isApproved=1)
#     return render(request,"blog/blog_pending.html",{'approved':approved})

def intermediary(request):
    return render(request, "blog/test.html")

def pending_post(request):
    pending = Blog.objects.filter(isApproved=-1)
    return render(request,"blog/blog_pending.html",{'pending':pending})

# def delete_post(request, user_id):
#     if request.method == "POST":
#         post_id = request.POST.get('post_id')
#         post = get_object_or_404(Blog,id=post_id)
#         # post.delete()
#         return redirect('blog_home')

def delete_post(request, user_id):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Blog, id=post_id)
        if request.user.id == user_id:  
            post.delete() 
        else:
            print("Unauthorized deletion attempt by user:", request.user.id)

    return redirect('blog_home')