from django.urls import path
from products.views import ProductListView

urlpatterns = [
    path('listado/', ProductListView.as_view(), name='listado_productos'),
]