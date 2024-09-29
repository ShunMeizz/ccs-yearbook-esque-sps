from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
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
from .forms import SignUpForm, LogInForm
from .tokens import profile_token

import os
from uuid import uuid4

#def id_path_and_rename(path):
#    def wrapper(instance, filename):
#        ext = filename.split('.')[-1]
#        if instance.pk:
#            filename = '{}.{}'.format(instance.pk, ext)
#        else:
#            filename = '{}.{}'.format(uuid4().hex, ext)
#        return os.path.join(path, filename)
#    return wrapper
# Function to send email to proceed in setting up profile
def acc_verified_email(request, user, to_email):
    mail_subject = "Account Verified!"
    message = render_to_string("email_messages/acc_verified_message.html", {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': profile_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(mail_subject, message, to=[to_email])

    
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
        'user': user,
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
   # if request.user.is_authenticated:
     #   return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate the user until admin approval
            user.save()

             # Create UserAccount instance without setting verified status
            UserAccount.objects.create(
                user=user,
                id_front=form.cleaned_data['id_front'],
                id_back=form.cleaned_data['id_back'],
                is_acc_verified=False 
            )
            messages.success(request, "Thank you for signing up! Your account is under review by our admins.")
            #activate_email(request, user, form.cleaned_data.get('email'))  
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request): 
    #if request.user.is_authenticated:
     #   return redirect('home')
    form = LogInForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.first_name}! You have been logged in")
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
    return render(request, "home.html", {
        "name": f"{request.user.first_name} {request.user.last_name}"
    })