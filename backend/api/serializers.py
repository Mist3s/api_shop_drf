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
    """Serializer упаковки."""
    class Meta:
        model = Packing
        fields = ('id', 'name', 'weight')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class ProductPackingSerializer(serializers.ModelSerializer):
    """Serializer упаковки в продукте для вывода данных."""
    name = serializers.CharField(source='packing.name')
    weight = serializers.IntegerField(source='packing.weight')

    class Meta:
        model = ProductPacking
        fields = (
            'name',
            'weight',
            'price',
        )


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer изображения."""
    image = Base64ImageField()

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'preview')


class PackingAmountSerializer(serializers.ModelSerializer):
    """Serializer упаковки в продукте для ввода данных."""
    id = serializers.IntegerField(write_only=True)
    price = serializers.FloatField(write_only=True)

    class Meta:
        model = ProductPacking
        fields = ('id', 'price')


class ProductGetSerializer(serializers.ModelSerializer):
    """Serializer продукта для вывода данных."""
    packing = ProductPackingSerializer(
        source='product_packing',
        many=True,
        read_only=True
    )
    images = ProductImageSerializer(
        source='product_images',
        many=True
    )
    is_favorite = serializers.BooleanField(
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            'available',
            'is_favorite',
            'name',
            'slug',
            'category',
            'description',
            'packing',
            'created',
            'updated',
            'images'
        )


class ProductSerializer(serializers.ModelSerializer):
    """Serializer продукта для ввода данных."""
    packing = PackingAmountSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('slug', 'name', 'category', 'description', 'images', 'packing',)

    def to_representation(self, instance):
        """Переопределение serializer для выходных данных."""
        return ProductGetSerializer(
            instance, context=self.context
        ).data

    def create_and_update_objects(self, product, packaging, images):
        """Метод создания и обновления объекта."""
        images_list = []
        for image in images:
            new_images = ProductImage(
                product=product,
                image=image['image'],
                preview=image['preview'],
            )
            images_list.append(new_images)
        packaging_list = []
        for packing in packaging:
            new_packaging = ProductPacking(
                product=product,
                packing_id=packing['id'],
                price=packing['price'],
            )
            packaging_list.append(new_packaging)
        ProductPacking.objects.bulk_create(packaging_list)
        ProductImage.objects.bulk_create(images_list)
        return product

    def create(self, validated_data):
        """Создание продукта."""
        packaging = validated_data.pop('packing')
        images = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        return self.create_and_update_objects(
            product=product,
            packaging=packaging,
            images=images
        )

    def update(self, product, validated_data):
        """Обновление продукта."""
        if (not validated_data.get('packing')
                or not validated_data.get('images')):
            raise serializers.ValidationError(
                'Не все обязательные поля заполнены.'
            )
        product.packing.clear()
        product.product_images.all().delete()
        packaging = validated_data.pop('packing')
        images = validated_data.pop('images')
        product = super().update(product, validated_data)
        return self.create_and_update_objects(
            product=product,
            packaging=packaging,
            images=images
        )
