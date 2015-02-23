from django import template
register = template.Library()
from django.template.defaulttags import register

@register.filter
def qb_get_fields(dictionary, key):
  return dictionary.get(key)
