from django.shortcuts import render

# Create your views here.
def products_list(request):
    lista =[
        {"code": "xyz"},
        {"code": "123"}
    ] 
    
    context = {
        "products_list": lista
    }

    return render(request, "miApp/products_list.html", context)