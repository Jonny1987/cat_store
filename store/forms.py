from django import forms
from . import models

class ProductRequestForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    category = forms.ModelChoiceField(queryset=models.Category.objects)
    description = forms.CharField(label='description', max_length=100)
