from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.html import format_html

from .models import UserAccount
from .forms import SignUpForm, LogInForm, UpdateUserAccountForm
from .tokens import profile_token

import os
from uuid import uuid4

AuthUser = get_user_model()

# def account_activation(request, uidb64, token):
#     User = get_user_model()  # Use get_user_model() for flexibility
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
    
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()

#         messages.success(request, "Thank you for email confirmation. Now you can log in.")
#         return redirect('login')
#     else:
#         messages.error(request, "Activation link is invalid!")
    
#     return redirect('signup')

def acc_verified_email(request, user, to_email):
    mail_subject = "Account Verified!"
    message = render_to_string("email_messages/acc_verified_message.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': profile_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = "html"
    
    user.is_active = True
    user.save()

    if email.send():
        messages.success(
            request, 
            format_html('Dear <b>{}</b>, please check your email inbox at <b>{}</b> for your account status update. <b>Note:</b> Check your spam folder.', user, to_email)
        )
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def acc_not_verified_email(request, user, to_email):
    mail_subject = "Fail to create an account"
    message = render_to_string("email_messages/acc_not_verified_message.html", {
        'user': user.username,
    })
    email = EmailMessage(mail_subject, message, to=[to_email])

    if email.send():
        messages.success(
            request, 
            format_html('Dear <b>{}</b>, please check your email inbox at <b>{}</b> for your account status update. <b>Note:</b> Check your spam folder.', user, to_email)
        )
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate the user until admin approval
            user.save()

            messages.success(request, "Thank you for signing up! Your account is under review by our admins.")
            print(request.FILES)
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request): 
    form = LogInForm(data=request.POST)
    if request.method == "POST":
        print("Before valid")
        if form.is_valid():
            print("After valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(f"Attempting to authenticate user: {username}")
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username}! You have been logged in")
                return redirect('home')
            else:
                print("Authentication failed: User not found") 
                messages.error(request, "User not found, please sign in")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)  # Log out the user
    messages.info(request, "Logged out successfully!")  # Optional message
    return redirect('login') 

@login_required
def home_view(request):
    if (request.user.is_superuser):
        return render(request, "admin_home.html")
    return render(request, "home.html", {
        "name": f"{request.user.username}"
    })

@login_required
def account_view(request):
    user = UserAccount.objects.get(pk = request.user.id)

    if (not user):
        return redirect('login')

    if (request.method == 'POST'):
        form = UpdateUserAccountForm(request.POST, instance = user)

        if (form.is_valid()):
            form.save()

            return redirect('account')
        
    else:
        form = UpdateUserAccountForm(instance = user)

    return render(request, 'user_account/account.html', {'form': form})