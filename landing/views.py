from django.views.generic import ListView
from .models import *


class Index(ListView):
    model = Headers
    template_name = 'index.html'

    def get_queryset(self):
        return Headers.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['inspires'] = Inspires.objects.filter(is_published=True)
        context['lets'] = Lets.objects.filter(is_published=True)
        context['crm'] = Crm.objects.filter(is_published=True)
        context['gallery'] = Galleries.objects.filter(is_published=True)
        context['reviews_header'] = ReviewsHeader.objects.filter(is_published=True)
        context['reviews1'] = Reviews.objects.filter(is_published=True)[:1]
        context['reviews2'] = Reviews.objects.filter(is_published=True)[1:2]
        context['reviews3'] = Reviews.objects.filter(is_published=True)[2:3]
        return context
