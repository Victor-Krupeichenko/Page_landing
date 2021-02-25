from django import template
from blog.models import Notes

register = template.Library()

@register.inclusion_tag('sidebar.html')
def popular_notes(cnt=3):
    notes = Notes.objects.order_by('-views')[:cnt]
    return {'notes':notes}
