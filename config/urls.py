"""config URL Configuration

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
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy

from blog.models import Post, CategoryPost
from products.models import Product, Category

info_dict = {
    # 'queryset': Post.objects.all(),
    # 'queryset': CategoryPost.objects.all(),
    # 'queryset': Product.objects.all(),
    # 'queryset': Category.objects.all(),
    'queryset': [
            Post.objects.all(), CategoryPost.objects.all(),
            Product.objects.all(), Category.objects.all(),
                 ]
}


urlpatterns = [
    # i18n_patterns(
    path('admin/', admin.site.urls),  # Django admin
    path('accounts/', include('allauth.urls')),  # URL Auth
    path('', include('pages.urls')),  # index
    path(gettext_lazy('products/'), include('products.urls', namespace='shop')),  # shop
    path(gettext_lazy('cart/'), include('cart.urls', namespace='cart')),  # Cart
    path(gettext_lazy('blog/'), include('blog.urls')),  # blog
    path('sitemap.xml', sitemap,  # sitemap
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    # )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # uploads

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),  # optimize tool
    ] + urlpatterns
