from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

CHOICES_LIST = ((1, '1',), (2, '2',), (3, '3',), (4, '4',), (5, '5',))


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название категории')
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey('Category', related_name='products', verbose_name='Категории',
                                 on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фотография товара', upload_to='products_img')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    products = models.ManyToManyField('Product', related_name='articles', verbose_name='Товары')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', blank=True, null=True,
                                related_name='comments_products')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    rating = models.IntegerField(default=False, verbose_name='Рейтинг', choices=CHOICES_LIST)
