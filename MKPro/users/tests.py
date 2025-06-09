from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()

class UsersAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_password = 'testpass123'
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password=self.user_password
        )
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')
        self.index_url = reverse('index')  # Se asume que la URL "index" existe
        self.productos_url = reverse('listado_productos')
        self.password_reset_url = reverse('password_reset')
        self.password_change_url = reverse('password_change')

    # --------------------------
    # Tests de Signup (Registro)
    # --------------------------
    def test_signup_creates_user_and_redirects(self):
        signup_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newuserpass123',
            'password2': 'newuserpass123',
        }
        response = self.client.post(self.signup_url, signup_data)
        new_user = User.objects.filter(username='newuser').first()
        self.assertIsNotNone(new_user)
        self.assertRedirects(response, self.login_url)

    # --------------------------
    # Tests de Login
    # --------------------------
    def test_login_valid_credentials(self):
        login_data = {
            'username': self.user.username,
            'password': self.user_password
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

    def test_login_invalid_credentials(self):
        login_data = {
            'username': self.user.username,
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, login_data)
        # Se espera que se renderice el template con un mensaje de error en español
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Por favor, introduzca un nombre de usuario y clave correctos")

    # --------------------------
    # Tests de Logout
    # --------------------------
    def test_logout(self):
        self.client.login(username=self.user.username, password=self.user_password)
        # Se usa POST para logout, ya que en la plantilla se define un formulario POST.
        response = self.client.post(self.logout_url)
        self.assertRedirects(response, self.login_url)
        self.assertNotIn('_auth_user_id', self.client.session)

    # --------------------------
    # Tests de Actualización de Perfil
    # --------------------------
    def test_profile_update_redirects_with_next(self):
        self.client.login(username=self.user.username, password=self.user_password)
        new_data = {
            'username': self.user.username,
            'email': self.user.email,
            'first_name': 'Updated',
            'last_name': 'User'
        }
        next_url = self.index_url  # Ejemplo: redirigir a index
        response = self.client.post(f"{self.profile_url}?next={next_url}", data=new_data)
        self.assertRedirects(response, next_url)

    def test_profile_update_redirects_without_next(self):
        self.client.login(username=self.user.username, password=self.user_password)
        new_data = {
            'username': self.user.username,
            'email': self.user.email,
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.post(self.profile_url, data=new_data)
        # Se redirige a la URL por defecto (por ejemplo, index)
        self.assertRedirects(response, self.index_url)

    def test_profile_update_invalid_data(self):
        self.client.login(username=self.user.username, password=self.user_password)
        invalid_data = {
            'username': self.user.username,
            'email': 'invalid-email',  # Email mal formado
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.post(self.profile_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        # Mensaje en español según la validación del formulario.
        self.assertContains(response, "Ingrese una dirección de correo electrónico válida")

    def test_profile_data_persistence(self):
        self.client.login(username=self.user.username, password=self.user_password)
        new_first_name = "NewFirst"
        new_last_name = "NewLast"
        new_email = "updated@example.com"
        new_data = {
            'username': self.user.username,
            'email': new_email,
            'first_name': new_first_name,
            'last_name': new_last_name,
        }
        response = self.client.post(self.profile_url, data=new_data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, new_email)
        self.assertEqual(self.user.first_name, new_first_name)
        self.assertEqual(self.user.last_name, new_last_name)

    def test_profile_requires_authentication(self):
        self.client.logout()
        response = self.client.get(self.profile_url)
        expected_redirect = f"{self.login_url}?next={self.profile_url}"
        self.assertRedirects(response, expected_redirect)

    # --------------------------
    # Tests de Cambio de Contraseña
    # --------------------------
    def test_password_change(self):
        self.client.login(username=self.user.username, password=self.user_password)
        change_data = {
            'old_password': self.user_password,
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        }
        response = self.client.post(self.password_change_url, change_data)
        password_change_done_url = reverse('password_change_done')
        self.assertRedirects(response, password_change_done_url)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword123'))

    def test_password_change_invalid_old_password(self):
        self.client.login(username=self.user.username, password=self.user_password)
        change_data = {
            'old_password': 'wrong_old_password',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        }
        response = self.client.post(self.password_change_url, change_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Su contraseña antigua es incorrecta")

    # --------------------------
    # Tests de Restablecimiento de Contraseña (Password Reset)
    # --------------------------
    def test_password_reset_sends_email(self):
        reset_data = {
            'email': self.user.email
        }
        response = self.client.post(self.password_reset_url, reset_data)
        password_reset_done_url = reverse('password_reset_done')
        self.assertRedirects(response, password_reset_done_url)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertIn(self.user.email, email.to)

    def test_password_reset_confirm(self):
        # Aseguramos que no haya un usuario autenticado.
        self.client.logout()
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_confirm_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        # Realizamos la llamada GET a la URL de confirmación
        response_get = self.client.get(reset_confirm_url)
        # Si el GET devuelve un 302, usamos la URL de redirección como destino del POST.
        if response_get.status_code == 302:
            post_url = response_get['Location']
            response_get2 = self.client.get(post_url)
            self.assertEqual(response_get2.status_code, 200)
        else:
            post_url = reset_confirm_url
            self.assertEqual(response_get.status_code, 200)
        # Preparamos los datos para la nueva contraseña
        new_password_data = {
            'new_password1': 'finalnewpass123',
            'new_password2': 'finalnewpass123',
        }
        # Enviamos el POST a la URL adecuada
        response_post = self.client.post(post_url, new_password_data)
        # Esperamos que se redirija a la URL de confirmación final (password_reset_complete)
        password_reset_complete_url = reverse('password_reset_complete')
        self.assertRedirects(response_post, password_reset_complete_url)
        # Refrescamos el objeto usuario y comprobamos que la contraseña se actualizó
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('finalnewpass123'))