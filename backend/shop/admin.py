from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Category, Product, Packing,
    ProductPacking, ProductImage
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Количество дополнительных полей для загрузки изображений


class PackagingInline(admin.TabularInline):
    model = ProductPacking
    extra = 3  # Количество дополнительных полей для добавления упаковки


@admin.display(description='Изображение')
def display_image(obj):
    return mark_safe(f'<img src="{obj.image.url}" height="60" />')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (display_image, 'product')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'available',
        'created', 'updated'
    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available',]
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, PackagingInline]


@admin.register(Packing)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight']
