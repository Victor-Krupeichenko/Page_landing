from django import template
from landing.models import InspireHeader, Inspires

register = template.Library()


@register.inclusion_tag('_inc/inspire_title.html')
def show_titles():
    title = InspireHeader.objects.filter(is_published=True)
    return {'title': title}


@register.inclusion_tag('_inc/inspire_content.html')
def show_content():
    contents = Inspires.objects.filter(is_published=True)[:1]
    contents_1 = Inspires.objects.filter(is_published=True)[1:]
    return {'contents': contents,
            'contents_1': contents_1}

@register.inclusion_tag('_inc/inspire_design.html')
def show_design():
    design = Inspires.objects.values('attainment_title', 'attainment_content').filter(is_published=True)
    return {'design':design}
