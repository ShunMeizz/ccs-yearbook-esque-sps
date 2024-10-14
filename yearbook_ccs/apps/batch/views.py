from django.shortcuts import get_object_or_404, render
from ..profiles.models import UserProfile

# Create your views here.
def batch_page_view(request):
    user_profile = get_object_or_404(UserProfile, user_account=request.user)

    user_program = user_profile.program
    user_batch_year = user_profile.batch_year

    # filter profiles based on current user's program and batch year
    filtered_profiles = UserProfile.objects.filter(
        program=user_program,
        batch_year=user_batch_year
    )

    context = {
        'filtered_profiles': filtered_profiles,
        'user_profile': user_profile
    }

    return render(request, 'batch/batch_page.html', context)