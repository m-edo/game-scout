from itertools import product
from django import forms
from ecommerce.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'