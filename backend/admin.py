from django.contrib import admin
from backend.models import *
# admin.site.unregister(User)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'products')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_products', 'creation_date')
    list_filter = ('creation_date',)


# @admin.unregister(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
