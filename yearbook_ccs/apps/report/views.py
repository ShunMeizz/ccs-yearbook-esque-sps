from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from apps.report.forms import ReportForm
from .models import Report

# Create your views here.
def report_home(request):
    username = request.user.username
    # tapol ko so ang paglabay og multiple forms sa ni
    post_reports = Report.objects.filter(report_type=0).all()
    comment_reports = Report.objects.filter(report_type=1).all()
    profile_reports = Report.objects.filter(report_type=2).all()

    form = ReportForm()
    if request.method == 'POST':
        print("TEst")
    
    return render(request, 'reports.html',{'post_reports':post_reports,
                                            'profile_reports':profile_reports,
                                            'comment_reports':comment_reports,
                                            'username':username,
                                            'form':form})

def add_report(request):
    print("POST REPORT")
    if request.method == "POST" and request.POST.get('action') == 'report':
        # Create a new report instance
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
