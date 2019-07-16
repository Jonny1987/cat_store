from django.test import TestCase
from django.urls import reverse

from store.models import Product, Category


class StoreHomeViewTests(TestCase):
    def test_no_products(self):
        response = self.client.get(reverse('store:home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products'], [])

    def test_one_product(self):
        cat = Category.objects.create(name='test')
        cat.save()
        prod = Product.objects.create(name='test', description='test', price=1, category=cat)
        prod.save()
        url = reverse('store:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products'], [repr(prod)])

