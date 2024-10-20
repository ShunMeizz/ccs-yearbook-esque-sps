from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from apps.profiles.models import UserProfile
# from apps.blog import Blog TODO: uncomment this
from apps.user_management.models import UserAccount
from .models import ProfileComment
from .forms import CommentCreationForm, ProfileCommentCreationForm, BlogCommentCreationForm

# Create your views here.
def comment(request):
    profile = get_object_or_404(UserProfile, pk = 1)
    comments = profile.profile_comments.all()

    return render(request, 'comment_test.html', {'comments': comments})

def create_profile_comment(request, profile_id):
    profile_id = get_object_or_404(UserProfile, pk = profile_id)

    if request.method == "POST":
        form = ProfileCommentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = profile_id
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def create_blog_comment(request, blog_id):
    blog_id = get_object_or_404(Blog, pk = blog_id)

    if request.method == "POST":
        form = BlogCommentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog_id
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_comment(request, comment_id):
    comment = get_object_or_404(ProfileComment, pk = comment_id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit_comment(request, comment_id):
    comment = get_object_or_404(ProfileComment, pk = comment_id)
    if request.method == "POST":
        form = CommentCreationForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))