from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib import messages

from ..user_management.tokens import profile_token
from .forms import ProfileCreationForm
from .models import UserProfile
from ..user_management.models import UserAccount

# Create your views here.
def profiles_home(request):
    profile = UserProfile.objects.get(user_account = request.user)
    if (request.method == "POST"):
        update_profile_form = ProfileCreationForm(request.POST, request.FILES)
        if update_profile_form.is_valid():
            profile = form.save(commit=False)
            profile.user_account = request.user
            profile.save()

            return redirect('profile_home')
    else:
        form = ProfileCreationForm()
            
    return render(request, 'profiles/profiles_home.html', {'update_pform': form, 'profile': profile})

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

        login(request, user) #automatically logs in user to sign up
        messages.success(request, "Thank you for pressing the link. Now you can set up your profile.")
        return redirect('setup_profile_2')
    else:
        messages.error(request, "Link is invalid!")
    
    return redirect('signup')

def setup_profile_2_view(request):
    User = get_user_model()
    user = User.objects.get(pk=request.user.id)
    if (request.method == "POST"):
        form = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_account = user
            profile.save()

            print(user)

            return redirect('profile_home')
    else:
        form = ProfileCreationForm()
            
    return render(request, 'profiles/setup_profile.html', {'form': form})
