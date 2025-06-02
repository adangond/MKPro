from django.db import models
from django.core.exceptions import ValidationError

#Validacion de datos ingresados

def validate_positive(value):
    if value < 0:
        raise ValidationError('El valor no puede ser negativo')
    
# Create your models here.
class Products(models.Model):    
    description = models.TextField(max_length=250)
    category = models.TextField(max_length=250, null=True, blank=True, default=None)
    product_class = models.TextField(max_length=250, null=True, blank=True, default=None)
    product_type = models.TextField(max_length=250, null=True, blank=True, default=None)
    product_UM = models.TextField(max_length=15, null=True, blank=True, default="Unid.")
    
    def __str__(self):
        return f"{self.description}, {self.category}, {self.product_class}, {self.product_type}, {self.product_UM}"
    

class Inventory(models.Model):
    product = models.OneToOneField('Products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0) # Impide valores negativos
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive]) # Valida el ingreso de valores negativos

    def __str__(self):
        return f"{self.product.description} - Stock: {self.quantity}, Costo Promedio: {self.average_cost}"