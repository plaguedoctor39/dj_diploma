from django.contrib import admin
from backend.models import *


# admin.site.unregister(User)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'products')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'display_products', 'creation_date')
#     list_filter = ('creation_date',)


# @admin.unregister(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
