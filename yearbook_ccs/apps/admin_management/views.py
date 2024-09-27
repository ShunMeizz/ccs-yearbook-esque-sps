from django.shortcuts import render
from ..user_management.models import UserAccount

# Create your views here.
def review_user_account(request):
    account = UserAccount.objects.filter(is_verified=False)
    return render(request, 'review_acc/review_account.html', {'account': account})
