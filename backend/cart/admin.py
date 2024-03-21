from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Регистрация модели корзины в админке."""
    list_display = [
        'id', 'user', 'product', 'quantity'
    ]
