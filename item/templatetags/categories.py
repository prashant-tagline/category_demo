from django import template
from ..models import SubCategory, Category, Item
register = template.Library()

@register.inclusion_tag('navbar.html')
def navbar():
    categories = Category.objects.filter(parent_category_id__isnull=True)   
    sub_categories = SubCategory.objects.exclude(parent_category_id__isnull=True)        
    context = {
        'categories':categories,
        'sub_categories':sub_categories,
    }
    return context