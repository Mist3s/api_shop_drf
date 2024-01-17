from django.db import models
from django.urls import reverse


class PublishedBaseModel(models.Model):
    """Абстрактная модель.
    Добавляет флаг available и created/updated."""
    available = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        blank=False,
        help_text='Снимите галочку, чтобы скрыть.'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        blank=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        blank=False
    )

    class Meta:
        abstract = True


class Category(PublishedBaseModel):
    """Модель категории."""
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Укажите название категорию',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Slug',
        help_text='Укажите slug категории'
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category',
            args=[self.slug]
        )

    def __str__(self):
        return self.name


class Product(PublishedBaseModel):
    """Модель продукта"""
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Укажите категорию товара'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Укажите название товара'
    )
    slug = models.CharField(
        max_length=200,
        verbose_name='Slug',
        help_text='Укажите slug товара',
    )
    description = models.TextField(
        blank=True,
        max_length=500,
        verbose_name="Описание товара",
        help_text='Добавьте описание к товару'
    )
    packaging = models.ManyToManyField(
        'Packaging',
        through='ProductPackaging',
        related_name='product',
        verbose_name='Упаковка',
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[self.pk, self.slug]
        )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """Модель изображений продуктов."""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        related_name='product_images',
        help_text='Укажите продукт'

    )
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Выберите изображение продукта',
        upload_to='product/%Y/%m/%d/'
    )

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продукта'

    def __str__(self):
        return str(self.pk)


class Packaging(models.Model):
    """Модель упаковки"""
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Укажите название',
    )
    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Вес',
        help_text='Вес упаковки в граммах'
    )

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'

    def __str__(self):
        return self.name


class ProductPackaging(PublishedBaseModel):
    """Вспомогательная модель: Продукт - Упаковка."""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_packaging',
        verbose_name='Продукт',
        help_text='Укажите продукт'
    )
    packaging = models.ForeignKey(
        Packaging,
        on_delete=models.CASCADE,
        related_name='product_packaging',
        verbose_name='Упаковка',
        help_text='Укажите упаковку'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        help_text='Цена этой упаковки за 1 шт.'
    )

    class Meta:
        verbose_name = 'Продукт - Упаковка'
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(
            fields=['product', 'packaging'],
            name='unique_product_packaging'
        )]
