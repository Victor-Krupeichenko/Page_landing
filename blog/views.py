from braces.views import MessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import F, Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.views.generic.list import MultipleObjectMixin
from .models import Notes, BlogCategories, Tags, CommentNotes
from .forms import CommentForm, NotesAddForm, RegisterUserForm, UserLoginForm


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


class DeleteCommit(MessageMixin, DeleteView):
    model = CommentNotes
    template_name = 'views_notes.html'
    success_message = "Комментарий удалён"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('detail_notes', kwargs={'slug': self.object.note.slug})


class CreatedNotes(CreateView):
    form_class = NotesAddForm
    template_name = '_inc/form_add_notes.html'

    def get_context_data(self, **kwargs):
        context = super(CreatedNotes, self).get_context_data(**kwargs)
        context['title'] = 'Создать запись'
        return context


class DeleteNotes(MessageMixin, DeleteView):
    model = Notes
    template_name = 'views_notes.html'
    success_url = reverse_lazy('blog')
    success_message = "Запись успешна удалена"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)


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

    def get_context_data(self, **kwargs):
        context = super(CommentsUpdate, self).get_context_data(**kwargs)
        context['title'] = f"Обновить комментарий: {CommentNotes.objects.get(pk=self.kwargs['pk'])}"
        return context


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(RegisterUserView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        return context

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class UserLogin(LoginView):
    template_name = 'login_user.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


class UserLogout(LogoutView):
    next_page = reverse_lazy('home')
