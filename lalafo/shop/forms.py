from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_product', 'category', 'price', 'description', 'active', 'phone_number', 'image']