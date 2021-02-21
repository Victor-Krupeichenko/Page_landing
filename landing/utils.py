from django.contrib import messages
from django.shortcuts import redirect
from .forms import FormQuestionsViews
from django.views.generic import CreateView, ListView
from .models import ReviewsAddText


class MyMixinFormLanding(CreateView):
    form_class = FormQuestionsViews
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = FormQuestionsViews(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.cleaned_data['name']}, Ваш вопрос получен!")
            return redirect('home')
        else:
            messages.error(request, 'Ошибка получения')
            return redirect('home')


class MyMixinFormReviewsAdd(ListView):
    model = ReviewsAddText
    template_name = 'reviews_add.html'

    def get_queryset(self):
        return ReviewsAddText.objects.filter(is_published=True)
