# products/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Products

User = get_user_model()

class ProductTests(TestCase):
    def setUp(self):
        self.username = 'produser'
        self.password = 'prodpass'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        # Crea un producto de prueba. Asegúrate de que el modelo Products tenga los campos usados.
        self.product = Products.objects.create(
            description='Producto de prueba',
            category='Categoría de prueba',
            product_class='Clase de prueba',
            product_type='Tipo de prueba',
            price=100,
            product_UM='uds',
            status=True,
            # Supongamos que tienes un campo 'quantity' para cantidad disponible.
            quantity=10
        )

    def test_product_list_view_redirect_if_not_logged_in(self):
        """
        Verifica que si no estás autenticado, se redirija a la página de login.
        """
        response = self.client.get(reverse("listado_productos"))
        login_url = reverse("login")
        expected_url = f'{login_url}?next={reverse("listado_productos")}'
        self.assertRedirects(response, expected_url)

    def test_product_list_view_access_logged_in(self):
        """
        Con autenticación, la lista de productos se debe mostrar correctamente.
        """
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("listado_productos"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista de Productos")
        # Verifica que el producto de prueba aparezca en la respuesta.
        self.assertContains(response, self.product.description)
        self.assertContains(response, self.product.quantity)