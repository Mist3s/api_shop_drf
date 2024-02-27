from rest_framework import serializers

from shop.models import Category, Product, ProductImage, Packaging, ProductPackaging


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class PackagingSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='product_packaging.name')
    # weight = serializers.FloatField(source='product_packaging.weight')
    # price = serializers.FloatField(source='product_packaging.price')

    class Meta:
        model = Packaging
        fields = (
            'name',
            'weight',
            # 'price'
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'preview')


class ProductSerializer(serializers.ModelSerializer):
    packaging = PackagingSerializer(
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
            'packaging',
            'created',
            'updated',
            'images'
        )
