from .forms import FormQuestionsViews
from django.urls import reverse_lazy
from django.views.generic import CreateView

class MyFormLanding(CreateView):
    form_class = FormQuestionsViews
    template_name = 'index.html'
    success_url = reverse_lazy('home')
