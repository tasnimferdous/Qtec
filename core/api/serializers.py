from rest_framework import serializers
from core.models import (
    Category,
    Brand,
    Seller,
    Warranty,
    Discount,
    Product
)

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Brand
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Seller
        fields = '__all__'


class WarrantySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Warranty
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Discount
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = True, read_only=True)
    brand = BrandSerializer(read_only=True)
    seller = SellerSerializer(read_only=True)
    warranty = WarrantySerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)


    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image',
                'category', 'brand', 'seller', 'warranty', 'discount']
