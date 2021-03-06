"""products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.utils.translation import gettext_lazy

from .views import SearchResultsListView, product_detail, product_list

app_name = 'shop'

urlpatterns = [
    # path('', CategoryListView.as_view(), name='category_list'),
    # path('<uuid:pk>/', ProductListView.as_view(), name='product_list'),
    path('', product_list, name='product_list'),
    path(gettext_lazy('<slug:category_slug>/'), product_list,
         name='product_list_by_category'),
    path(gettext_lazy('details/<uuid:id>/'), product_detail,
         name='product_detail'),
    # path('<uuid:pk>/<uuid:pk>', ProductDetailView.as_view(),
    #      name='product_detail'),
    path(gettext_lazy('search/'), SearchResultsListView.as_view(),
         name='search-results'),
]
