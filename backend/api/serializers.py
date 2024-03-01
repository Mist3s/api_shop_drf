from rest_framework import serializers

from shop.models import (
    Category, Product, ProductImage,
    Packing, ProductPacking
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class PackingSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'preview')


class ProductSerializer(serializers.ModelSerializer):
    packaging = PackingSerializer(
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
