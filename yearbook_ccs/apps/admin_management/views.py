from django.shortcuts import render, redirect
from ..user_management.models import UserAccount
from ..user_management.views import acc_not_verified_email, acc_verified_email
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_active and u.is_superuser, login_url='login') # This makes sure that the user is a superuser and an active user, if they fail to pass the test, they will be redirected to login.
def admin_dashboard(request):
    user_verified_count = UserAccount.objects.filter(is_acc_verified=True).count()
    user_unverified_count = UserAccount.objects.filter(is_superuser=False, is_acc_verified=False).count()

    return render(request, 'admin_home.html', {'user_verified_count': user_verified_count, 'user_unverified_count': user_unverified_count})

@user_passes_test(lambda u: u.is_active and u.is_superuser, login_url='login') 
def review_user_verification_requests(request):
    accounts = UserAccount.objects.filter(is_superuser=False, is_acc_verified=False)

    if request.method == 'POST':
        verified_user_ids = request.POST.getlist('verified_user_ids')
        not_verified_user_ids = request.POST.getlist('not_verified_user_ids')

        for user_id in verified_user_ids:
            try:
                user = UserAccount.objects.get(id=user_id)
                user.is_acc_verified = True
                user.is_active = True
                user.save()
                acc_verified_email(request, user, user.email)
            except UserAccount.DoesNotExist:
                continue

        for user_id in not_verified_user_ids:
            try:
                user = UserAccount.objects.get(id=user_id)
                acc_not_verified_email(request, user, user.email)
                user.delete()
            except UserAccount.DoesNotExist:
                continue

        return redirect('review_acc')

    return render(request, 'users/review_account.html', {'accounts': accounts})

@user_passes_test(lambda u: u.is_active and u.is_superuser, login_url='home')
def view_user_accounts(request):
    if (not request.user.is_superuser):
        return redirect('home')
    
    accounts = UserAccount.objects.filter(is_acc_verified=True)

    return render(request, 'users/user_verified_page.html' , {'useraccounts': accounts})

