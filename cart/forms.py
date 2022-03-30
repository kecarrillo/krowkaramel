# cart/forms.py
from django import forms

# Quantity from 1 to 99 999 products
PRODUCT_QUANTITY_CHOICES = [(int, str(i)) for i in range(1, 20)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
            choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update_product = forms.BooleanField(required=False, initial=False,
                                        widget=forms.HiddenInput)
