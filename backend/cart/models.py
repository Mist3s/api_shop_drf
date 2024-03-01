from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from shop.models import ProductPackaging
from users.models import User

MAX_QUANTITY_PRODUCT_AT_CART = 1000
MIN_QUANTITY_PRODUCT_AT_CART = 1


class Cart(models.Model):
    """Модель корзины."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Пользователь которому принадлежит корзина."
    )
    product = models.ForeignKey(
        ProductPackaging,
        on_delete=models.CASCADE,
        related_name='product_cart',
        verbose_name='Продукт',
        help_text='Выберите продукт который нужно добавить в корзину.'

    )
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=MIN_QUANTITY_PRODUCT_AT_CART,
            ),
            MaxValueValidator(
                limit_value=MAX_QUANTITY_PRODUCT_AT_CART
            )
        ],
        verbose_name='Количество',
        help_text='Количество продукта в корзине.'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(
            fields=['user', 'product'],
            name='unique_product_user_cart'
        )]
