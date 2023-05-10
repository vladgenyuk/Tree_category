from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')
    list_display_links = ('id', 'title', 'parent')
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'cost', 'created_at', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
