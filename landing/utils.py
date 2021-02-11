from .forms import FormQuestionsViews
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import ReviewsAddText

class MyFormLanding(CreateView):
    form_class = FormQuestionsViews
    template_name = 'index.html'
    success_url = reverse_lazy('home')

class MyFormReviewsAdd(ListView):
    model = ReviewsAddText
    template_name = 'reviews_add.html'

    def get_queryset(self):
        return ReviewsAddText.objects.filter(is_published=True)
