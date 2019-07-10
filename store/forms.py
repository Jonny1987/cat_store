from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    category = forms.ModelChoiceField(queryset=Product.objects)
