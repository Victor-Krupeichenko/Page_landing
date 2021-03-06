from django import forms
from .models import CommentNotes

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentNotes
        fields = ['name', 'email', 'text']
