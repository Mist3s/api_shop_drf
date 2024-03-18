from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from shop.models import ProductPacking
from users.models import User

MAX_QUANTITY_PRODUCT_AT_ORDER = 1000
MIN_QUANTITY_PRODUCT_AT_ORDER = 1


class Address(models.Model):
    region = models.CharField(
        max_length=150,
        verbose_name='Регион (область, край)',
        help_text='Укажите регион.'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        help_text='Укажите город доставки.'
    )
    street = models.CharField(
        max_length=150,
        verbose_name='Улица',
        help_text='Укажите улицу.'
    )
    house = models.CharField(
        max_length=30,
        verbose_name='Номер дома',
        help_text='Укажите номер дома.'
    )
    room = models.IntegerField(
        verbose_name='Номер квартиры',
        help_text='Укажите номер квартиры.'
    )


class Order(models.Model):
    """Модель заказа."""
    address = models.ForeignKey(
        Address,
        related_name='order_address',
        on_delete=models.CASCADE,
        verbose_name='Адрес доставки.'
    )
    user = models.ForeignKey(
        User,
        related_name='order_user',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан',
        help_text='Дата создания.'
    )
    update = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлено',
        help_text='Дата последнего обновления.'
    )
    paid = models.BooleanField(
        default=False,
        verbose_name='Статус оплаты'
    )

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ #{self.pk}'


class OrderItem(models.Model):
    """Позиция в заказе."""
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        ProductPacking,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(
                limit_value=MIN_QUANTITY_PRODUCT_AT_ORDER,
            ),
            MaxValueValidator(
                limit_value=MAX_QUANTITY_PRODUCT_AT_ORDER
            )
        ],
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        constraints = [models.UniqueConstraint(
            fields=['order', 'product'],
            name='unique_product_order'
        )]

    def __str__(self):
        return str(self.pk)
