# core/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CoreViewsTests(TestCase):
    def setUp(self):
        self.username = 'coreuser'
        self.password = 'pass123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_index_view_redirect_if_not_logged_in(self):
        """
        Sin autenticación, se debe redirigir a la página de login.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 302)
        # Comprueba que la redirección sea a login
        self.assertTrue(response.url.startswith(reverse("login")))

    def test_index_view_access_logged_in(self):
        """
        Con autenticación, se debe acceder a la vista index sin redirección.
        """
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        # Opcional: Verifica algún contenido esperado en la página
        self.assertContains(response, "MKPro")