from django.urls import reverse_lazy
from django.views import generic
from .models import Products
from .forms import ProductForm
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')  


class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('listado_productos')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProductListView(generic.ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = "products"