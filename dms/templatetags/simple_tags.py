from django.urls import reverse 
from django import template


register = template.Library()

@register.simple_tag()
def intralink(main, link):
    return reverse(main) + '#' + link
