from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q, ForeignKey, CharField, TextField
from django.db.models.fields import NOT_PROVIDED
from ..user_management.models import UserAccount
from ..report.models import Report
from ..profiles.models import UserProfile
from ..profiles.forms import ProfileCreationForm
from ..blog.models import Blog
from ..user_management.views import acc_not_verified_email, acc_verified_email

def admin_dashboard(request):
    if (not request.user.is_superuser):
        return redirect('home')

    user_verified_count = UserAccount.objects.filter(is_acc_verified=True).count()
    user_unverified_count = UserAccount.objects.filter(is_superuser=False, is_acc_verified=False).count()
    blog_reports_count = Report.objects.filter(report_type=0, status=0).count()
    profile_reports_count = Report.objects.filter(report_type=2, status=0).count()
    comment_reports_count = Report.objects.filter(report_type=1, status=0).count()

    return render(request, 'admin_home.html', 
                  {'user_verified_count': user_verified_count, 
                   'user_unverified_count': user_unverified_count,
                   'blog_reports_count': blog_reports_count, 
                   'profile_reports_count': profile_reports_count, 
                   'comment_reports_count': comment_reports_count
                   })

def review_user_verification_requests(request):
    if (not request.user.is_superuser):
        return redirect('home')
    
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
    
    elif request.method == 'GET':
        search = request.GET.get('search', '')

        accounts = accounts.filter(
            Q(username__icontains=search) | Q(email=search) | Q(school_id_number__icontains=search) 
        )

    return render(request, 'admin/review_account.html', {'accounts': accounts})

def view_user_accounts(request):
    if (not request.user.is_superuser):
        return redirect('home')

    accounts = UserAccount.objects.filter(is_acc_verified=True)

    if request.method == 'GET':
        search = request.GET.get('search', '')
        accounts = accounts.filter(
            Q(username__icontains=search) | Q(profile__first_name__icontains=search) | 
            Q(profile__last_name__icontains=search) | Q(email=search) | Q(school_id_number__icontains=search) 
        )
    
    
    return render(request, 'admin/user_verified_page.html' , {'useraccounts': accounts})

def edit_profile(request, profile_id):
    if (not request.user.is_superuser ):
        return redirect('home')
    
    profile = get_object_or_404(UserProfile, id=profile_id)
    
    if (request.method == "POST"):
        form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            print("form is valid")
            form.save()

            # return redirect('edit_profile', profile_id=profile_id)
    else:
        form = ProfileCreationForm(instance=profile)

    return render(request, 'profiles/profiles_home.html', {'update_pform': form, 'profile': profile})

def set_default_profile(request, profile_id):
    if (not request.user.is_superuser ):
        return redirect('home')
    
    profile = UserProfile.objects.get(id=profile_id)
    for field in profile._meta.get_fields():
        if not field.auto_created and field.editable:  # Exclude autogenerated and non-editable fields
            if isinstance(field, ForeignKey):
                continue

            if field.name == "program" or field.name == "batch_year":
                continue
            elif field.default != NOT_PROVIDED:
                field_value = field.get_default() if callable(field.get_default) else field.default
            elif field.null and isinstance(field, (CharField, TextField)) and (field.name != "first_name" or field.name != "last_name"):
                field_value = ""
            elif field.name == "profile_pic":
                field_value = "media/profile_pictures/default_graduate.png"
            else:
                continue

            setattr(profile, field.name, field_value)

    profile.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def manage_blogs(request):
    if (not request.user.is_superuser):
        return redirect('home')
    
    posts = Blog.objects.all()

    return render(request, 'admin/manage_blogs.html', {'posts': posts})