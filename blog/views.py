from django.db.models import F
from django.views.generic import ListView, DetailView
from .models import Notes, BlogCategories, Tags


class NotesViews(ListView):
    model = Notes
    template_name = 'blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesViews, self).get_context_data(**kwargs)
        context['title'] = 'My Blog'
        return context

    def get_queryset(self):
        return Notes.objects.filter(is_published=True)


class NotesByCategories(ListView):
    template_name = 'blog.html'
    allow_empty = False

    def get_queryset(self):
        return Notes.objects.filter(category__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesByCategories, self).get_context_data(**kwargs)
        context['title'] = BlogCategories.objects.get(slug=self.kwargs['slug'])
        return context


class ViewsNotes(DetailView):
    model = Notes
    template_name = 'views_notes.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super(ViewsNotes, self).get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class NotesTags(ListView):
    model = Notes
    template_name = 'blog.html'

    def get_queryset(self):
        return Notes.objects.filter(tag__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesTags, self).get_context_data(**kwargs)
        context['title'] = f"Записи по тегу: {Tags.objects.get(slug=self.kwargs['slug'])}"
        return context
