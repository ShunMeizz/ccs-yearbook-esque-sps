from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from apps.report.forms import ReportForm
from apps.user_management.models import UserAccount
from apps.profiles.models import UserProfile
from .models import Report

# Create your views here.

# This makes sure that the user is a superuser and an active user, if they fail to pass the test, they will be redirected to login.
# @user_passes_test(lambda u: u.is_active and u.is_superuser, login_url='login')
def report_home(request):
    # tapol ko so ang paglabay og multiple forms sa ni
    post_reports = Report.objects.filter(report_type=0).all()
    comment_reports = Report.objects.filter(report_type=1).all()
    profile_reports = Report.objects.filter(report_type=2).all()
    reported_profiles = []
    for pr in profile_reports:
        profile = UserProfile.objects.get(id = pr.report_item_id)
        reported_profiles.append(profile)

    print("PROFILE REPORTS",(reported_profiles))
    return render(request, 'reports_home.html',{'post_reports':post_reports,
                                            'profile_reports':profile_reports,
                                            'comment_reports':comment_reports,
                                            'reported_profiles':reported_profiles})

def add_report(request):
    print("POST REPORT")
    if request.method == "POST":
        report_item_id = request.POST.get('report_item_id')
        report = Report(
            reason=request.POST.get('report_reason'),
            report_type=request.POST.get('report_type'),
            link=request.META.get('HTTP_REFERER') + "post/" + report_item_id,
            user_reported_id=request.user.id,
            report_item_id = report_item_id
        )
        report.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'reports.html')  # Fallback render if not POST

def finished_report(request):
    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        report = get_object_or_404(Report,pk=report_id)
        report.status = 1
        report.save()
        print('Finished report')
        print(report_id)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))