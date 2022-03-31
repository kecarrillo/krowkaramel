from django.urls import path
from django.utils.translation import gettext_lazy

from . import views
from .views import blog_category

urlpatterns = [
    path('', views.menu, name='menu'),
    path(gettext_lazy('<str:category>/'), blog_category, name='blog_category'),
]
