from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import (
    Category,
    Brand,
    Seller,
    Warranty,
    Discount,
    Product
)

from core.api.serializers import (
    CategorySerializer,
    BrandSerializer,
    SellerSerializer,
    WarrantySerializer,
    DiscountSerializer,
    ProductSerializer,
)

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

