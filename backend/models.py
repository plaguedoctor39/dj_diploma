from django.contrib.auth.models import AbstractUser, User
from django.db import models

CHOICES_LIST = ((1, '1',), (2, '2',), (3, '3',), (4, '4',), (5, '5',))
# class User(AbstractUser):
#     pass


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    categories = models.ManyToManyField('Category', related_name='products', verbose_name='Категории')
    photo = models.ImageField(verbose_name='Фотография товара', upload_to='products_img')

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


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', blank=True, null=True, related_name='comments_products' )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    rating = models.IntegerField(default=False, verbose_name='Рейтинг', choices=CHOICES_LIST)


class Cart(models.Model):
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
