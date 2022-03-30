from django.urls import path
from . import views
from .views import blog_category

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<str:category>/', blog_category, name='blog_category'),
]
