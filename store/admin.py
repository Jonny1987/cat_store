from django.contrib import admin

from .models import Category, Product, ProductRequest

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'displayed')
    list_filter = ('displayed',)
    search_fields = ('description',)

@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
