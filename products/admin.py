# products/admin.py
from django.contrib import admin

from .models import Product, Flavour, Allergen, Category, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    inlines = [
            ReviewInline,
    ]
    list_display = ("category", "name", "price", "stock", "available")
    list_filter = ("category", "name", "price", "stock", "available")
    list_editable = ("price", "stock",)



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Flavour)
admin.site.register(Allergen)
