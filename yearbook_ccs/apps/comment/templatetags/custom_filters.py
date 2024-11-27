from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def timesince_first_part(value):
    time_str = timesince(value)
    return time_str.split(',')[0]  # Get the first part before the comma