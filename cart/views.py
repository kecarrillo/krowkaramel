# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.
def cart_detail(request):
    """
    Method to get the cart content.

    :param request: HTTP request.
    :type request: HttpRequest
    :return: Get the cart content.
    :rtype: any
    """
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'], 'update_product': True}
        )
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    """
    Method to get products add to the cart and apply update.

    :param request: HTTP request (POST).
    :type request: HttpRequest
    :param product_id: Id of the added product.
    :type product_id: int
    :return: Get products add to the cart and apply update.
    :rtype: any
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned = form.cleaned_data
        cart.add_product(product=product, quantity=cleaned['quantity'],
                         update_quantity=cleaned['update_quantity'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """
    Method to withdraw a product from the cart.

    :param request: HTTP request (POST).
    :type request: HttpRequest
    :param product_id: Id of the added product.
    :type product_id: int
    :return: Withdraw a product from the cart.
    :rtype: any
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_product(product)
    return redirect('cart:cart_detail')
