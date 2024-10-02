from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import BlogForm

# Create your views here.
def blog_home(request):
    return render(request, 'blog/blog_home.html')

def blog_post(request):
    return render(request,"blog_post.html")

def get_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            post_msg = form.cleaned_data["post_msg"]
            return HttpResponseRedirect("/thanks/")
    else:
        form = BlogForm()
        return render(request, 'blog/blog_home.html', {'form': form})