from django.contrib import admin
from django.urls import  path, include

from rest_framework import routers

from store.api_views import ProductViewSet, ProductRequestList, ProductRequestDetail
from store import views

app_name = 'store'

router = routers.DefaultRouter()

router.register('products', ProductViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/product_requests', ProductRequestList.as_view()),
    path('api/v1/product_requests/<int:pk>', ProductRequestDetail.as_view()),
    path('', views.HomeView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('request/', views.request_product, name='request'),
    path('multiple_request/', views.multiple_request, name='multiple_request'),
    path('request_confirm/', views.request_confirm, name='request_confirm'),
]
