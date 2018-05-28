from django import forms

from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['name', 'text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['answer']
