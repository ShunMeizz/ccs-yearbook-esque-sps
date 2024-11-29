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
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount
from .forms import SignUpStep1Form, SignUpStep2Form, LogInForm, UpdateUserAccountForm
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

def acc_not_verified_email(request, user, to_email):
    mail_subject = "Fail to create an account"
    message = render_to_string("email_messages/acc_not_verified_message.html", {
        'user': user.username,
    })
    EmailMessage(mail_subject, message, to=[to_email])


def signup_step1(request):
    if request.method == 'POST':
        form = SignUpStep1Form(request.POST)
        if form.is_valid():
            # Store only the non-sensitive data in session
            step1_data = {key: value for key, value in form.cleaned_data.items() if key not in ['password1', 'password2']}
            request.session['step1_data'] = step1_data
            
            # Store the password separately (it's ok because session data is stored server-side)
            request.session['password1'] = form.cleaned_data['password1']
            return redirect('signup_step2')
        else:
             for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignUpStep1Form()

    return render(request, 'registration/signup_step1.html', {'form': form})

def signup_step2(request):
    step1_data = request.session.get('step1_data', None)
    if not step1_data:
        return redirect('signup_step1')

    # Retrieve the passwords from session
    password1 = request.session.get('password1')

    if request.method == 'POST':
        form = SignUpStep2Form(request.POST, request.FILES)
        if form.is_valid():
            # Combine Step 1 and Step 2 data to create the user instance
            user_data = {**step1_data, **form.cleaned_data}
            user = UserAccount(**user_data)
            user.set_password(password1)
            user.save()

            del request.session['step1_data']
            del request.session['password1']
            message = "Thank you for signing up!"
            additional_message = "Your account is under review. We will notify you at your email user.email? inbox (or spam folder) for the verification update."
            return render(request, 'message.html', {'message': message, 'additional_message': additional_message})
        else:
             for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignUpStep2Form()

    return render(request, 'registration/signup_step2.html', {'form': form})

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
                if not user.is_acc_verified:
                    message = "Account still under review"
                    additional_message = "Check your email inbox (or spam folder) for the verification update sent by the admin"
                    return render(request, 'message.html', {'message': message, 'additional_message': additional_message})
                
                
                login(request, user)
                messages.success(request, f"Hello {user.username}! You have been logged in")
                return redirect('home')
            else:
                messages.error(request, "User not found, please sign in")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request) 
    messages.info(request, "Logged out successfully!") 
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