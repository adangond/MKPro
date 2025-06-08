from django import forms
from .models import Products
from PIL import Image


class ProductForm(forms.Form):
    description = forms.CharField(max_length=250, label="Descripción", required=True)
    category = forms.CharField(max_length=250, label="Categoria", required=False) 
    product_class = forms.CharField(max_length=250, label="Clase", required=False) 
    product_type = forms.CharField(max_length=250, label="Tipo", required=False) 
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio Unitario", required=True)
    product_UM = forms.CharField(max_length=15, label="Unidad de medida", required=False)
    status = forms.CharField(initial=True, label="Disponible", required=True) 
    photo = forms.ImageField(label="Imagen", required=False) 
    #created_at = forms.CharField(label="Fecha de creación", required=False)
    #updated_at = forms.CharField(label="Última actualizació", required=False)
    

    def save(self):
        product = Products.objects.create(
            description=self.cleaned_data['description'],
            category=self.cleaned_data['category'],
            product_class=self.cleaned_data['product_class'],
            product_type=self.cleaned_data['product_type'],
            price=self.cleaned_data['price'],
            product_UM=self.cleaned_data['product_UM'],
            status=self.cleaned_data['status'],
            photo=self.cleaned_data['photo']
        )

        # 🔹 Redimensionar imagen si se sube una
        if product.photo:
            ruta_imagen = product.photo.path
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((500, 500), Image.ANTIALIAS)
            imagen.save(ruta_imagen)

        return product