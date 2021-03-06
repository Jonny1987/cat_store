from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    displayed = models.BooleanField()

    def __str__(self):
        return self.name


class ProductRequest(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    owner = models.ForeignKey('auth.User', related_name='product_requests', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
