from django.contrib import admin
from .models import Products  

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'description', 
        'category', 
        'product_class', 
        'product_type', 
        'status', 
        'price', 
        'product_UM',
        'quantity',      # Nuevo campo
        'average_cost',  # Nuevo campo
        'photo', 
        'created_at', 
        'updated_at'
    )
    search_fields = ('description', 'category')
    list_filter = ('category',)
    
    fieldsets = (
        (None, {
            'fields': (
                'description', 
                'category', 
                'product_class', 
                'product_type', 
                'price', 
                'product_UM', 
                'status', 
                'photo'
            )
        }),
        ('Inventario', {
            'fields': ('quantity', 'average_cost'),
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Products, ProductsAdmin)


