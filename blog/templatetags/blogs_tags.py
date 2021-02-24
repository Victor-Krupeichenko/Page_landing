from django import template
from django.db.models import Count, F
from blog.models import BlogCategories

register = template.Library()


@register.inclusion_tag('category.html')
def views_categories(category_select=0):
    categories = BlogCategories.objects.annotate(cnt=Count('category', filter=F('category__is_published'))).filter(
        cnt__gt=0)
    return {'categories': categories, 'category_select': category_select}
