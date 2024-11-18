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
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.report_type = request.POST.get('report_type')
            report.link = request.path
            report.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ReportForm()
    return render(request, 'component/report_modal.html',{'form':form})
