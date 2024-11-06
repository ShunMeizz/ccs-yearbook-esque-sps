from django.shortcuts import render, redirect
from ..user_management.models import UserAccount
from ..user_management.views import acc_not_verified_email, acc_verified_email

def admin_dashboard(request):
    return render(request, 'admin_home.html')

def review_user_account(request):
    accounts = UserAccount.objects.filter(is_acc_verified=False)

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
            except UserAccount.DoesNotExist:
                continue

        return redirect('review_acc')

    return render(request, 'review_acc/review_account.html', {'accounts': accounts})



