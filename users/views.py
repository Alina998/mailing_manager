from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mailing_app:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'alina.pastaeva@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('mailing_app:home')

class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('mailing_app:home')
