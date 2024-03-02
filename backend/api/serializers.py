import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

from shop.models import (
    Category, Product, ProductImage,
    Packing, ProductPacking
)


class Base64ImageField(serializers.ImageField):
    """Кастомный тип поля изображений."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            _format, img_str = data.split(';base64,')
            ext = _format.split('/')[-1]
            data = ContentFile(
                base64.b64decode(img_str), name='temp.' + ext
            )
        return super().to_internal_value(data)


class PackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packing
        fields = ('id', 'name', 'weight')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class ProductPackingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='packing.name')
    weight = serializers.FloatField(source='packing.weight')

    class Meta:
        model = ProductPacking
        fields = (
            'name',
            'weight',
            'price',
        )


class ProductImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'preview')


class ProductSerializer(serializers.ModelSerializer):
    packing = ProductPackingSerializer(
        source='product_packing',
        many=True
    )
    images = ProductImageSerializer(
        source='product_images',
        many=True
    )

    class Meta:
        model = Product
        fields = (
            'available',
            'name',
            'slug',
            'category',
            'description',
            'packing',
            'created',
            'updated',
            'images'
        )
