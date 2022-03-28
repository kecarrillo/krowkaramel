# products/views.py
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available='AV')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'products/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
                                available="AV")
    return render(request,
                  'products/product_detail.html',
                  {'product': product})


# Create your views here.
class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'products/category_list.html'


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class SearchResultsListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/search_results.html'

    def get_queryset(self):
        query =  self.request.GET.get('q')
        return Product.objects.filter(
                Q(name__icontains=query) | Q(name__icontains=query)
        )
