from django.shortcuts import render, get_object_or_404

from .models import Product
from . import forms

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product(request, id):
    product = get_object_or_404(Product, pk=id)

    return render(request, 'product.html', {'product': product})
