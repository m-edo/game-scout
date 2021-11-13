from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('product', views.product, name='product'),
]
