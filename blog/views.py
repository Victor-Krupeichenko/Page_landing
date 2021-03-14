from django.contrib import messages
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.base import View
from django.views.generic.list import MultipleObjectMixin
from .models import Notes, BlogCategories, Tags, CommentNotes
from .forms import CommentForm, NotesAddForm


class NotesViews(ListView):
    model = Notes
    template_name = 'blog.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesViews, self).get_context_data(**kwargs)
        context['title'] = 'My Blog'
        context['category_select'] = 0
        return context

    def get_queryset(self):
        return Notes.objects.filter(is_published=True)


class NotesByCategories(ListView):
    template_name = 'blog.html'
    allow_empty = False
    paginate_by = 4

    def get_queryset(self):
        return Notes.objects.filter(category__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesByCategories, self).get_context_data(**kwargs)
        context['title'] = BlogCategories.objects.get(slug=self.kwargs['slug'])
        context['category_select'] = context['object_list'][0].category_id
        return context


class DetailNote(DetailView, MultipleObjectMixin):
    model = Notes
    template_name = 'views_notes.html'
    context_object_name = 'notes'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        object_list = Notes.get_no_parent(self.object)
        context = super(DetailNote, self).get_context_data(object_list=object_list, **kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class NotesTags(ListView):
    model = Notes
    template_name = 'blog.html'
    paginate_by = 5

    def get_queryset(self):
        return Notes.objects.filter(tag__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesTags, self).get_context_data(**kwargs)
        context['title'] = f"Записи по тегу: {Tags.objects.get(slug=self.kwargs['slug'])}"
        return context


class Search(ListView):
    template_name = 'blog.html'
    paginate_by = 4

    def get_queryset(self):
        return Notes.objects.filter(Q(title__icontains=self.request.GET.get('search')) |
                                    Q(content__icontains=self.request.GET.get('search')))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&"
        return context


class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        note = Notes.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.note = note
            form.save()
            messages.success(request, "Ваш комментарий добавлен")
            return redirect(note.get_absolute_url())
        else:
            messages.error(request, 'Ошибка добовления комментария')
            return redirect(note.get_absolute_url())


def delete_messages(request, pk):
    comment = CommentNotes.objects.get(pk=pk)
    comment.delete()
    messages.success(request, 'комментарий удалён')
    return HttpResponse('<script>history.back();</script>')


class CreatedNotes(CreateView):
    form_class = NotesAddForm
    template_name = '_inc/form_add_notes.html'

    def get_context_data(self, **kwargs):
        context = super(CreatedNotes, self).get_context_data(**kwargs)
        context['title'] = 'Создать запись'
        return context


def delete_notes(request, slug):
    note = Notes.objects.get(slug=slug)
    note.delete()
    messages.success(request, 'Запись удалена')
    return redirect('blog')


class NotesUpdate(UpdateView):
    model = Notes
    form_class = NotesAddForm
    template_name = '_inc/form_add_notes.html'

    def get_context_data(self, **kwargs):
        context = super(NotesUpdate, self).get_context_data(**kwargs)
        context['title'] = f"Редактировать запись: {Notes.objects.get(slug=self.kwargs['slug'])}"
        context['update'] = True
        return context


class CommentsUpdate(UpdateView):
    model = CommentNotes
    form_class = CommentForm
    template_name = '_inc/form_update_comment.html'
