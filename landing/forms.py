from django import forms
from .models import FormQuestions


class FormQuestionsViews(forms.ModelForm):
    class Meta:
        model = FormQuestions
        fields = ['questions', 'name', 'email']
        widgets = {
            'questions': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
