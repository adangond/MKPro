from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Products

class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = "products"