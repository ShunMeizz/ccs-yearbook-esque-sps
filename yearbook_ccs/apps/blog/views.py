from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from apps.profiles.models import UserProfile
from apps.user_management.models import UserAccount
from .models import Blog
from .forms import BlogForm, FilterForm
from django.db.models import Q  

@login_required
def blog_home(request):
    print("blog post")
    user_profile = get_object_or_404(UserProfile, user_account=request.user)
    #posts = get_post()
    posts = filter_post(request)
    action = request.POST.get('action')
    filterform = FilterForm(request.GET)
    # filterform = FilterForm()    
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
        if action == "filter":
            print("filter")
            filterform, posts = filter_post(request) # Get posts without filters
    else:
        form = BlogForm()
    
     # Get the filter parameters, or default to user's batch year and program
    batch_year = request.GET.get('year') or user_profile.batch_year
    program = request.GET.get('program') or user_profile.program
    all_batch_years = UserProfile.objects.values_list('batch_year', flat=True).distinct()
    available_programs = UserProfile.objects.values_list('program', flat=True).distinct()

    # Filter profiles
    filtered_timeline = UserProfile.objects.filter(
        batch_year=batch_year, program=program
    ).select_related('user_account')

    return render(request, "blog/blog_home.html", {
        'form': BlogForm(),
        'posts': posts,
        'filtered_timeline': filtered_timeline,
        'all_batch_years': all_batch_years,
        'available_programs': available_programs,
        'filterform': filterform
    })

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
            return render(request,"blog/blog_user.html",{'pending':pending,'user':user})
    else:
        return render(request,"blog/blog_user.html",{'pending':pending,'user':user})

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
    program = request.GET.get('program') 
    year = request.GET.get('year') 
    
    filtered_posts = Blog.objects.all().order_by("-date")

    if program:
        user_prog = UserProfile.objects.filter(program=program).values_list("user_account", flat=True)
        filtered_posts = filtered_posts.filter(user_id__in=list(user_prog))
    if year:
        filtered_posts = filtered_posts.filter(user__profile__batch_year=year)
    
    return filtered_posts

# comments part huehue
def load_comments(request,post_id):
    post = get_object_or_404(UserProfile, id=post_id)
    comments = post.blog_comments.all()
    return render(request,"blog/components/blog_post_comment.html",{'comments':comments})


@login_required
def blog_search(request):
    """Redirect to search results based on user input."""
    query = request.GET.get('search', '').strip()

    if query:
        matching_profiles = UserProfile.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(user_account__username__icontains=query)
        )
        matching_accounts = [profile.user_account for profile in matching_profiles]
        posts = Blog.objects.filter(user__in=matching_accounts).order_by("-date")
    else:
        posts = Blog.objects.none()

    return render(request, 'blog/blog_search.html', {
        'posts': posts,
        'query': query,
    })