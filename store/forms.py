from django import forms
from django.core.validators import RegexValidator

from . import models


class ProductRequestForm(forms.ModelForm):
    name = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z0-9]+$', 'Only letters and numbers are allowed')])

    class Meta:
        model = models.ProductRequest
        fields = ['name', 'category', 'description', 'image']


class MultipleRequestForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=5)
