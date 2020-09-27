from cooker_app.models import Category

from django.core.cache import cache
from django.db.models.aggregates import Count
from django import template

#register = template.Library()
#@register.inclusion_tag('includes/sidebar_menu.html')

def get_sidebar_menu(request):
    context = {}
    context['categoryes'] = Category.objects.all()
    return context
