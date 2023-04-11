from django import forms
from .models import Question
from django.db import models
from .models import Feedback


class JobForm(forms.Form):
    job_title = forms.CharField(label='Job Title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label='Company Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.DecimalField(label='Salary', max_digits=8, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo_upload = forms.ImageField(label='Logo', widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(label='Location', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    choose_field = forms.ChoiceField(label='Choose Field', choices=[('Design & creative', 'Design & creative'), ('Design & development', 'Design & development'), ('sales & marketing', 'sales & marketing'
    ),('mobile Application','mobile Application'),('construction','construction'),('Information technology','Information technology')], widget=forms.Select(attrs={'class': 'form-control'}))


class QuestionForm(forms.ModelForm):
     class Meta:
        model = Question
        fields = ['question_text', 'answer_1', 'answer_2', 'answer_3', 'answer', 'choose_field']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'answer_1': forms.TextInput(attrs={'class': 'form-control'}),
            'answer_2': forms.TextInput(attrs={'class': 'form-control'}),
            'answer_3': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
            'choose_field': forms.Select(attrs={'class': 'form-control'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback',)
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 5}),
        }

# class QuizResult(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     score = models.IntegerField()
#     timestamp = models.DateTimeField(auto_now_add=True)  
  




 
