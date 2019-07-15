from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory

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

        return redirect('request_confirm')

    elif request.method == 'GET':

        single_form = forms.ProductRequestForm()
        multiple_form = forms.MultipleRequestForm()

        return render(request, 'request_product.html', {'product_form': single_form, 'multiple_form': multiple_form})

def request_confirm(request):
    return render(request, 'request_confirm.html')

def multiple_request(request):
    if request.method == 'POST':
        RequestFormSet = formset_factory(forms.ProductRequestForm)
        filled_formset = RequestFormSet(request.POST)

        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['name'])
            filled_formset.save()
        return redirect('request_confirm')
    else:
        filled_form = forms.MultipleRequestForm(request.GET)

        if filled_form.is_valid():
            number_of_requests = filled_form.cleaned_data['number']

        RequestFormSet = formset_factory(forms.ProductRequestForm, extra=number_of_requests)
        formset = RequestFormSet()
        return render(request, 'multiple_request.html', {'formset': formset})
