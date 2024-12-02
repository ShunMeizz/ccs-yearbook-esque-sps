from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now
from datetime import timedelta

register = template.Library()

@register.filter
def timesince_first_part(value):
    time_str = timesince(value)
    return time_str.split(',')[0] + ' ago' # Get the first part before the comma


@register.filter
def show_date_or_naturaltime(value):
    """
    Show the real date if the given date is more than 2 days old.
    Otherwise, show the naturaltime.
    """
    if value is None:
        return ""  # Return an empty string if value is None

    current_time = now()
    if current_time - value > timedelta(days=2):
        return value.strftime('%B %d, %Y')  # Format the date
    else:
        return timesince_first_part(value)