# custom_filters.py
from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_months(value, months):
    """
    Add a specified number of months to a given date.
    """
    try:
        return value + timedelta(days=months * 30)
    except:
        return None