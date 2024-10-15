from django.shortcuts import render
from apps.profiles.models import UserProfile
from apps.user_management.models import UserAccount
from .models import ProfileComment

# Create your views here.
def comment(request):
    comments = ProfileComment.objects.all()

    return render(request, 'comment_test.html', {'comments': comments, 'user': request.user})
