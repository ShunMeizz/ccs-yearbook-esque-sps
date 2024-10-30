from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from apps.profiles.models import UserProfile
from .models import Blog

from .forms import BlogForm, FilterForm

@login_required
def blog_home(request):
    print("blog post")
    posts = get_post()
    action = request.POST.get('action')    
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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if action == "filter":
            print("filter")
            filterform, posts = filter_post(request) # Get posts without filters
    else:
        form = BlogForm()
        filterform = FilterForm()
        
    return render(request, "blog/blog_home.html", {'form': form, 'posts': posts, 'filterform': filterform})

# TEMP TO SHOW ALL BLOGS WITHOUT FILTER FROM ISAPPROVED. 
# TO BE DELETED AFTER ISAPPROVED FILTERS ARE WORKING AND DONE
def get_post():
    print("all posts",Blog.objects.all().order_by("-date"))
    return Blog.objects.all().order_by("-date")

def intermediary(request):
    return render(request, "blog/test.html")

def my_post(request, user_id):
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

def filter_post(request):
    if request.method == "POST":
        filterform = FilterForm(request.POST)
        if filterform.is_valid():
            program = filterform.cleaned_data.get('prog')
            if not program:
                return FilterForm(), get_post()
            else:
                user_prog = UserProfile.objects.filter(program__in=program).values_list("user_account", flat=True)
                # print("user ids:")
                # print(user_prog)
                # print(list(user_prog))
                    
                filtered_program = Blog.objects.filter(user_id__in=list(user_prog)).order_by("-date")
                # print(filtered_program)
                return filterform, filtered_program
    else:
        filterform = FilterForm()

    return filterform, None