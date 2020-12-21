from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from backend.forms import CommentForm
from backend.models import Product, Category, Comments
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    cart_product_form = CartAddProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        template = 'shop/product/smartphones.html',
    else:
        template = 'index.html'
    return render(request,
                  template,
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            author = request.user
            text = comment_form.cleaned_data['text']
            rating = comment_form.cleaned_data['rating']
            comments = Comments.objects.create(author=author, text=text, rating=rating, product=product)
            comment_form.save()
    else:
        comment_form = CommentForm
    return render(request,
                  'shop/product/phone.html',
                  {'product': product,
                   'form': comment_form,
                   'categories': categories,
                   'cart_product_form': cart_product_form})


def empty_page(request):
    categories = Category.objects.all()
    return render(request, 'shop/empty_section.html', {'categories': categories})
