from django.db import models
from django.core.exceptions import ValidationError

# Opciones predefinidas para el estado del producto
STATUS_CHOICES = [(True, 'Activo'), (False, 'Inactivo')]

# Función para validar que el valor sea positivo
def validate_positive(value):
    if value < 0:
        raise ValidationError('El valor no puede ser negativo')

class Products(models.Model):
    description = models.CharField(
        max_length=250,
        unique=True,
        verbose_name='Descripción'
    )
    category = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None,
        verbose_name='Categoría'
    )
    product_class = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None,
        verbose_name='Clase'
    )
    product_type = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None,
        verbose_name='Tipo'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=0,
        verbose_name='Precio Unitario'
    )
    product_UM = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default='Unid.',
        verbose_name='Unidad de Medida'
    )
    status = models.BooleanField(
        default=True,
        choices=STATUS_CHOICES,
        verbose_name='Estado'
    )
    photo = models.ImageField(
        upload_to='',
        null=True,
        blank=True,
        default='default.jpg',
        verbose_name='Imagen'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Actualización'
    )

    # Nuevos campos integrados de inventario
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Cantidad Disponible'
    )
    average_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[validate_positive],
        verbose_name='Costo Promedio'
    )

    def __str__(self):
        return (
            f"{self.description} - Categoría: {self.category} - Clase: {self.product_class} "
            f"- Tipo: {self.product_type} - Precio: {self.price} - UM: {self.product_UM} - "
            f"Estado: {'Activo' if self.status else 'Inactivo'} - Cantidad: {self.quantity} "
            f"- Costo Promedio: {self.average_cost} - Creado: {self.created_at} "
            f"- Última actualización: {self.updated_at}"
        )
