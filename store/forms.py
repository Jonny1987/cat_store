from django import forms
from . import models

class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = models.ProductRequest
        fields = ['name', 'category', 'description']
