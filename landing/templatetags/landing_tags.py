from django import template
from landing.models import InspireHeader, Inspires, Crm, CrmContent, GalleriesTitles, GalleryImages, ReviewsHeader, \
    Reviews

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
    return {'design': design}


@register.inclusion_tag('_inc/crm_title.html')
def show_title_crm():
    titles = Crm.objects.filter(is_published=True)
    return {'titles': titles}


@register.inclusion_tag('_inc/crm_sections.html')
def show_content_crm():
    content = CrmContent.objects.filter(is_published=True)
    return {'content': content}


@register.inclusion_tag('_inc/crm_video.html')
def show_videos():
    videos = CrmContent.objects.values('video').filter(is_published=True)
    return {'videos': videos}


@register.inclusion_tag('_inc/gallery_title.html')
def show_gallery_title():
    gallery_title = GalleriesTitles.objects.filter(is_published=True)
    return {'gallery_title': gallery_title}


@register.inclusion_tag('_inc/gallery_img.html')
def show_gallery_img():
    gallery_img = GalleryImages.objects.filter(is_published=True)[:1]
    gallery_img_1 = GalleryImages.objects.filter(is_published=True)[1:]
    return {'gallery_img': gallery_img,
            'gallery_img_1': gallery_img_1
            }

@register.inclusion_tag('_inc/reviews_title.html')
def show_reviews_title():
    titles = ReviewsHeader.objects.filter(is_published=True)
    return {'titles':titles}