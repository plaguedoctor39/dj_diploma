from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from backend.forms import AuthUserForm, RegisterUserForm


def main_page(request):
    return render(request, 'index.html')


def category_page(request):
    return render(request, 'smartphones.html')


def product_page(request):
    return render(request, 'phone.html')


def basket_page(request):
    return render(request, 'cart.html')


def empty_page(request):
    return render(request, 'empty_section.html')


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('main_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, email=email, password=password)
        login(self.request, auth_user)
        return form_valid


class MyLogout(LogoutView):
    next_page = reverse_lazy('main_page')