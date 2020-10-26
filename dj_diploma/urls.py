"""django_diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeListView.as_view(), name='main_page'),
    path('cart', views.basket_page, name='cart_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('login', views.MyLoginView.as_view(), name='login_page'),
    path('logout', views.MyLogout.as_view(), name='logout_page'),
    path('category/', views.category_page, name='category_page'),
    path('product/<int:pk>', views.ProductView.as_view(), name='product_page'),
    path('empty_section/', views.empty_page, name='empty_page'),
]
