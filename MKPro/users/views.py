from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


CustomUser = get_user_model()

class SignUpView(CreateView):
    """
    Vista para el registro de usuarios.
    """
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')  # Asegúrate de que 'login' esté definido en tus URLs

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')  # Buscar el parámetro GET 'next'
        if next_url:
            return next_url
        return reverse_lazy('index')
    
    def get_object(self, queryset=None):
        return self.request.user