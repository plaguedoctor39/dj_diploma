from django.contrib.auth.models import AbstractUser, User
from django.db import models


# class User(AbstractUser):
#     pass


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    categories = models.ManyToManyField('Category', related_name='products', verbose_name='Категории')
    photo = models.ImageField(verbose_name='Фотография товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    products = models.ManyToManyField('Product', related_name='articles', verbose_name='Товары')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField('Product', verbose_name='Товары')

    class Meta:
        verbose_name = 'Корзина'


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField('Product', verbose_name='Товары')
    creation_date = models.DateTimeField(verbose_name='Дата создания заказа')

    def display_products(self):
        return len([product.name for product in self.products.all()])
    display_products.short_description = 'Количество товаров'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
