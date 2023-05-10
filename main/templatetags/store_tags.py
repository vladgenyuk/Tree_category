from django import template
from main.models import *


register = template.Library()


@register.inclusion_tag('main/menu.html')
def draw_menu(category):
    context = {
        'category': category,
        'cats': Category.objects.filter(level__gt=1).select_related('parent'),
    }
    # context['cats_main'] = context['cats'].filter(parent__title=category)
    # print(context)
    return context
