from django.contrib import admin
from .models import Products, Inventory  # Importa el modelo de productos e inventario

# Register your models here. usuario:adangond, clave: 123

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'product_class', 'product_type', 'product_UM')
    search_fields = ('description', 'category')
    list_filter = ('category',)

admin.site.register(Products, ProductsAdmin)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'average_cost')
    search_fields = ('product__description',)
    list_filter = ('product__category',)

admin.site.register(Inventory, InventoryAdmin)
