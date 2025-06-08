from django.urls import path
from products.views import ProductFormView, ProductListView

urlpatterns = [
    path('listado', ProductListView.as_view(), name='listado_productos'),
    path('agregar/', ProductFormView.as_view(), name='agregar_producto'),   
]