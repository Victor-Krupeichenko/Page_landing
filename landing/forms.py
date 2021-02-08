from django import forms
from .models import FormQuestions


class FormQuestionsViews(forms.ModelForm):
    class Meta:
        model = FormQuestions
        fields = ['questions', 'name', 'email']
        widgets = {
            'questions': forms.TextInput(attrs={'class': 'form-control','placeholder':'Вопрос:'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя:'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email:'})
        }
