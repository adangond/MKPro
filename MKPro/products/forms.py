from django import forms
from .models import Products
from PIL import Image

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'description',
            'category',
            'product_class',
            'product_type',
            'price',
            'product_UM',
            'status',
            'photo',
        ]
        labels = {
            'description': 'Descripción',
            'category': 'Categoria',
            'product_class': 'Clase',
            'product_type': 'Tipo',
            'price': 'Precio Unitario',
            'product_UM': 'Unidad de medida',
            'status': 'Disponible',
            'photo': 'Imagen',
        }

    def save(self, commit=True):
        product = super().save(commit=commit)
        # Si se ha cargado una imagen, se redimensiona a 500x500 píxeles
        if product.photo:
            ruta_imagen = product.photo.path
            imagen = Image.open(ruta_imagen)
            # Nota: Image.ANTIALIAS está en desuso en versiones recientes de Pillow, puedes usar Image.LANCZOS si corresponde
            imagen = imagen.resize((500, 500), Image.ANTIALIAS)
            imagen.save(ruta_imagen)
        return product