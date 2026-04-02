from django.contrib import admin
from django.urls import path
from products.views import get_products

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', get_products),          # homepage
    path('products/', get_products),
]