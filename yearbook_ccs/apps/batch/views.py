
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from ..profiles.models import UserProfile
from django.db.models import Q  # For search queries

@login_required
def batch_page(request):
    """Display and filter profiles by batch year and program."""
    # Get the logged-in user's profile
    user_profile = get_object_or_404(UserProfile, user_account=request.user)

    # Get the filter parameters, or default to user's batch year and program
    batch_year = request.GET.get('year') or user_profile.batch_year
    program = request.GET.get('program') or user_profile.program

    # Filter profiles
    filtered_profiles = UserProfile.objects.filter(
        batch_year=batch_year, program=program
    ).select_related('user_account') #for me to access also the username
    
    # if social links are marked hidden, assigned as '' (dili lang None, ani lang '' para ka gets daw si html and js)
    for profile in filtered_profiles:
        profile.visible_social_links = {
            'facebook': profile.facebook_link if not profile.facebook_link_hidden else '',
            'linkedin': profile.linkedin_link if not profile.linkedin_link_hidden else '',
            'github': profile.github_link if not profile.github_link_hidden else '',
            'instagram': profile.instagram_link if not profile.instagram_link_hidden else '',
    }
    # Get distinct values for dropdowns
    all_batch_years = UserProfile.objects.values_list('batch_year', flat=True).distinct()
    available_programs = UserProfile.objects.values_list('program', flat=True).distinct()
    
    # Render the template with the filtered profiles and dropdown options
    return render(request, 'batch/batch_page.html', {
        'filtered_profiles': filtered_profiles,
        'all_batch_years': all_batch_years, # for batch year filter dropdown
        'available_programs': available_programs, # for program filter dropdown
        'user_profile': user_profile,
    })
@login_required
def search_profile(request):
    """Redirect to search results based on user input."""
    query = request.GET.get('search', '').strip()

    # Search by first name and/or last name using Q queries
    search_filters = Q(first_name__icontains=query) | Q(last_name__icontains=query)
    matching_profiles = UserProfile.objects.filter(search_filters).select_related('user_account') #for me to access also the username
    for profile in matching_profiles:
        profile.visible_social_links = {
            'facebook': profile.facebook_link if not profile.facebook_link_hidden else '',
            'linkedin': profile.linkedin_link if not profile.linkedin_link_hidden else '',
            'github': profile.github_link if not profile.github_link_hidden else '',
            'instagram': profile.instagram_link if not profile.instagram_link_hidden else '',
    }

    return render(request, 'batch/search_profile.html', {
        'profiles': matching_profiles,
        'query': query,
    })