from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from shop.models import ProductPacking

MAX_QUANTITY_PRODUCT_AT_ORDER = 1000
MIN_QUANTITY_PRODUCT_AT_ORDER = 1


class Order(models.Model):
    """Модель заказа."""
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        help_text='Ваше имя.'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        help_text='Ваша фамилия.'
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='Ваш email адрес.'
    )
    address = models.CharField(
        max_length=250,
        verbose_name='Адрес',
        help_text='Ведите адрес доставки.\n'
                  'Пример:\n'
                  'ул. Пушкина, д. 1, кв. 2'
    )
    postal_code = models.CharField(
        max_length=6,
        verbose_name='Почтовый индекс',
        help_text='Укажите ваш почтовый индекс.\n'
                  'Пример: 236238'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        help_text='Укажите город доставки.'
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

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.id.all())


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

    def get_cost(self):
        return self.price * self.quantity
