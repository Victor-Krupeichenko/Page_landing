from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .utils import MyFormLanding, MyFormReviewsAdd
from .forms import FormReviews


class Index(MyFormLanding, ListView):
    model = Headers
    template_name = 'index.html'

    def get_queryset(self):
        return Headers.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['title'] = 'Мой сайт'
        context['lets'] = Lets.objects.filter(is_published=True)
        context['crm'] = Crm.objects.filter(is_published=True)
        context['gallery'] = Galleries.objects.filter(is_published=True)
        context['reviews_header'] = ReviewsHeader.objects.filter(is_published=True)
        context['reviews1'] = Reviews.objects.filter(is_published=True)[:1]
        context['reviews2'] = Reviews.objects.filter(is_published=True)[1:2]
        context['reviews3'] = Reviews.objects.filter(is_published=True)[2:3]
        context['form_text'] = FormText.objects.filter(is_published=True)
        context['footer_img'] = FooterImages.objects.filter(is_published=True)
        return context


class ReviewsCreate(CreateView, MyFormReviewsAdd):
    form_class = FormReviews
    template_name = 'reviews_add.html'
    success_url = reverse_lazy('home')


class ReviewsAll(ListView):
    model = Reviews
    template_name = 'reviews_all.html'
    paginate_by = 8

    def get_queryset(self):
        return Reviews.objects.filter(is_published=True)


class InspireViews(DetailView):
    model = Inspires
    template_name = '_inc/inspire_single.html'
    context_object_name = 'inspire'

    def get_queryset(self):
        return Inspires.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(InspireViews, self).get_context_data(**kwargs)
        context['title'] = Inspires.objects.get(slug=self.kwargs['slug'])
        return context


class LetsViews(DetailView):
    model = Lets
    template_name = '_inc/lets_single_content.html'
    context_object_name = 'lets'

    def get_context_data(self, **kwargs):
        context = super(LetsViews, self).get_context_data(**kwargs)
        context['title'] = "Раздел Let's"
        return context
   