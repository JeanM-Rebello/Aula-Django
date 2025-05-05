from django import forms
from app_pages.models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'product_code', 'quantity', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
