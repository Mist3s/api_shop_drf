from django.contrib import admin

from .models import Order, OrderItem, Address, OrderStatus, DeliveryMethod


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


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    """Регистрация модели статуса заказа в админке."""
    list_display = [
        'name', 'slug'
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    """Регистрация модели способа доставки в админке."""
    list_display = [
        'name', 'slug', 'description'
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Регистрация модели заказа в админке."""
    list_display = [
        'id', 'user', 'address', 'paid',
        'created', 'update'
    ]
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInline]
    