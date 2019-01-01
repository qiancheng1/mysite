from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def multi(x, y):
    return x * y


@register.simple_tag
def multi(x, y):
    return x * y
