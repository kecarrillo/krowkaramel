# products/views.py
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Product, Category, ProductImage
from cart.forms import CartAddProductForm


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available='AV')
    images = ProductImage.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'products/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'images': images})


def product_detail(request, id_product):
    product = get_object_or_404(Product,
                                id=id_product,
                                available="AV")
    cart_product_form = CartAddProductForm()
    category = get_object_or_404(Category, name=product.category)
    return render(request,
                  'products/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'category': category})


class SearchResultsListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
                Q(name__icontains=query) | Q(name__icontains=query)
        )
