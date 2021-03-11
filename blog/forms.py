from django import forms
from .models import CommentNotes, Notes


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentNotes
        fields = ['name', 'email', 'text']


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
