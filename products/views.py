# products/views.py
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Product, Category
from cart.forms import CartAddProductForm


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(available='AV')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)

    paginator = Paginator(products_list,
                          per_page=8,
                          orphans=3,
                          allow_empty_first_page=True
                          )  # Show 8 products per page (min 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request,
                  'products/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
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
