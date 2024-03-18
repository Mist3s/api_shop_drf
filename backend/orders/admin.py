from django.contrib import admin

from .models import Order, OrderItem, Address


class OrderItemInline(admin.TabularInline):
    """Инлайн вывод позиций заказа."""
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Регистрация модели адреса в админке."""
    list_display = [
        'id', 'region', 'city', 'street',
        'house', 'room'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Регистрация модели заказа в админке."""
    list_display = [
        'id', 'user', 'address', 'paid',
        'created', 'update'
    ]
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInline]
    