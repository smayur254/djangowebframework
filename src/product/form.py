from django import forms
from product.models import Product

class CreateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = "__all__"
    