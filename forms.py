from django.db import models
from quitzapp.models import Questions
from django import forms


class Questions_Form(forms.ModelForm):
    class Meta:  # data about data#
        model = Questions
        fields = '__all__'
