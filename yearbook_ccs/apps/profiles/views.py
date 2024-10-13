from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib import messages

from ..user_management.tokens import profile_token

# Create your views here.
def profiles_home(request):
    return render(request, 'profiles/profiles_home.html')

# Setup profile view after user clicks the acc_verified_email (in user_management app) link
def setup_profile_view(request, uidb64, token):
    User = get_user_model()  # Use get_user_model() for flexibility
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and profile_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for pressing the link. Now you can set up your profile.")
        return redirect('profile_home') # TODO : change link for setting up profile
    else:
        messages.error(request, "Link is invalid!")
    
    return redirect('signup')


