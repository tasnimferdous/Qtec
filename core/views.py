from django.shortcuts import render
from .models import (
    Category,
    Brand,
    Seller,
    Warranty,
    Discount,
    Product
)

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    sellers = Seller.objects.all()
    warranty = Warranty.objects.all()
    discount = Discount.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
        'sellers': sellers,
        'warranty_list': warranty,
        'discount_list': discount,
    }
    return render(request, 'home.html', context)
