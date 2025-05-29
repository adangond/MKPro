from django.db import models

# Create your models here.
class Products(models.Model):    
    description = models.TextField(max_length=250)
    category = models.TextField(max_length=250, null=True, blank=True, default=None)
    product_class = models.TextField(max_length=250, null=True, blank=True, default=None)
    product_type = models.TextField(max_length=250, null=True, blank=True, default=None)
    product_UM = models.TextField(max_length=15, null=True, blank=True, default="Unid.")
    
    def __str__(self):
        return f"{self.description}, {self.category}, {self.product_class}, {self.product_type}, {self.product_UM}"