from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea
from django.contrib.auth.forms import AuthenticationForm
from .models import CommentNotes, Notes


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentNotes
        fields = ['name', 'email', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 4})
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class NotesAddForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'image', 'category', 'tag', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '--- Выберите категорию ---'
        self.fields['tag'].label = 'Теги'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name:'}))
    password1 = forms.CharField(help_text='(пароль должен содержать как минимум 8 символов)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password:'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'confirm password:'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email:'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class UserLoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'name:'
            self.fields['password'].widget.attrs['placeholder'] = 'password:'
