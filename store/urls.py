from django.contrib import admin
from django.urls import  path

from . import api_views
from . import views


urlpatterns = [
    path('api/v1/products/', api_views.ProductList.as_view()),
    path('admin/', admin.site.urls),
    path('product/<int:id>/', views.product, name='product'),
    path('request/', views.request_product, name='request'),
    path('multiple_request/', views.multiple_request, name='multiple_request'),
]
