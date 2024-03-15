from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Инлайн вывод позиций заказа."""
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Регистрация модели заказа в админке."""
    list_display = [
        'id', 'first_name', 'last_name', 'email',
        'address', 'postal_code', 'city', 'paid',
        'created', 'update'
    ]
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInline]
    