# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from products.models import Product

# Create your views here.


def client(request):
    return render(request, 'client/client.html')
