from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
from django.http import HttpResponseRedirect, HttpResponse
from apps.profiles.models import UserProfile
from apps.blog.models import Blog
from apps.user_management.models import UserAccount
from .models import Comment
from .forms import CommentCreationForm, ProfileCommentCreationForm, BlogCommentCreationForm

# Create your views here.
def comment(request):
    profile = get_object_or_404(UserProfile, pk = 1)
    comments = profile.profile_comments.all()

    # blog = get_object_or_404(Blog, pk = 1)
    # comments = blog.blog_comments.all()

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

            # To render the new comment without refreshing the page
            # csrf_token = get_token(request)
            
            # # Render new comment as HTML to insert into the page
            # comment_html = render_to_string('blog_comment.html', {'comment': comment, 'csrf_token': csrf_token, 'request':request})

            # # Return the new comment as HTML to insert into the page
            # return HttpResponse(comment_html)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.method == "POST":
        form = CommentCreationForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))