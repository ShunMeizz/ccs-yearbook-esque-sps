from django.shortcuts import render

# Create your views here.
def profiles_home(request):
    return render(request, 'profiles/profiles_home.html')
