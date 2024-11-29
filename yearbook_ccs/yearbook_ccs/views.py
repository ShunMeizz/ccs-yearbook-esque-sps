from django.http import HttpResponse
from django.shortcuts import render, redirect

import random

from apps.blog.models import Blog
from apps.profiles.models import UserProfile
def homepage(request):
    if (request.user.is_superuser):
        return redirect('admin_home')

    recent_blog = get_recent_blog()
    course = UserProfile.objects.filter(user_account_id=request.user.id).values_list('program',flat=True).first()
    course = "COMPUTER SCIENCE" if course == "BSCS" else "INFORMATION TECHNOLOGY" 
    
    if request.method == "POST":
        action = request.POST.get('course')
        print("mao ning action",action)
        course = "COMPUTER SCIENCE" if action == "BSCS" else "INFORMATION TECHNOLOGY" 

    
    
    return render(request,"home.html",{'recent_blog':recent_blog,'course':course})

def get_recent_blog():
    return Blog.objects.last()  

def get_random_profile():
    userIDs = UserProfile.objects.filter(program="BSCS").values_list('id', flat=True)
    userIDs = list(userIDs)
    return random.shuffle(userIDs)

# def get_course():
#     return UserProfile.objects.filter(program="BSCS")