from django.shortcuts import render
from .models import Report

# Create your views here.
def report_home(request):
    username = request.user.username
    # tapol ko so ang paglabay og multiple forms sa ni
    all_reports = Report.objects.all()
    return render(request, 'reports_home.html',{'all_reports':all_reports,'username':username})
