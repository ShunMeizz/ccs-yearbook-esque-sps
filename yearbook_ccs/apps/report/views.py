from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from apps.report.forms import ReportForm
from apps.user_management.models import UserAccount
from .models import Report

# Create your views here.

# This makes sure that the user is a superuser and an active user, if they fail to pass the test, they will be redirected to login.
# @user_passes_test(lambda u: u.is_active and u.is_superuser, login_url='login')
def report_home(request):
    # tapol ko so ang paglabay og multiple forms sa ni
    post_reports = Report.objects.filter(report_type=0).all().select_related('user_reported__profile')
    comment_reports = Report.objects.filter(report_type=1).all().select_related('user_reported__profile')
    profile_reports = Report.objects.filter(report_type=2).all().select_related('user_reported__profile')

    return render(request, 'reports_home.html',{'post_reports':post_reports,
                                            'profile_reports':profile_reports,
                                            'comment_reports':comment_reports})

def add_report(request):
    print("POST REPORT")
    if request.method == "POST":
        report = Report(
            reason=request.POST.get('report_reason'),
            report_type=request.POST.get('report_type'),
            link=request.META.get('HTTP_REFERER'),  # Save the referring page as the link
            user_reported_id=request.user.id
        )
            # Debugging prints
        print(f"Reason: {report.reason}")
        print(f"Report Type: {report.report_type}")
        print(f"Link: {report.link}")
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