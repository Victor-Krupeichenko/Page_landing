from django import template
from django.db.models import Count, F
from blog.models import BlogCategories

register = template.Library()


@register.inclusion_tag('sidebar_categories.html')
def views_categories():
    categories = BlogCategories.objects.annotate(cnt=Count('notes', filter=F('notes__is_published'))).filter(cnt__gt=0)
    return {'categories': categories}
