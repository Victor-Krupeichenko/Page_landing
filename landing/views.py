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
        return context
