from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from backend.forms import AuthUserForm, RegisterUserForm, CommentForm
from backend.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'list_products'


class ProductView(FormMixin, DetailView):
    model = Product
    template_name = 'phone.html'
    context_object_name = 'get_product'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('product_page', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def category_page(request):
    return render(request, 'smartphones.html')


def product_page(request):
    return render(request, 'phone.html')


def cart_page(request):
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
