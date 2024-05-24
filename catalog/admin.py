from django.contrib import admin

from catalog.models import Product, Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'unit_price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')
