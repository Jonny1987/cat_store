from django import forms
from . import models

class ProductRequestForm(forms.ModelForm):

    class Meta:
        model = models.ProductRequest
        fields = ['name', 'category', 'description']

class MultipleRequestForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=5)
