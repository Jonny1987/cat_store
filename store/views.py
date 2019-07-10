from django.shortcuts import render, get_object_or_404

from . import models
from . import forms

def home(request):
    products = models.Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product(request, id):
    product = get_object_or_404(models.Product, pk=id)

    return render(request, 'product.html', {'product': product})

def request_product(request):
    if request.method == 'POST':
        filled_form = forms.ProductRequestForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()

        return render(request, 'request_confirm.html')

    elif request.method == 'GET':

        form = forms.ProductRequestForm()

        return render(request, 'request_product.html', {'product_form': form})

def request_confirm(request):
    return render(request, 'request_confirm.html')
