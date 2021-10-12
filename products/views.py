from django.http import HttpRequest
from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request: HttpRequest):
    context = {
        "title": "Store"
    }
    return render(request, 'products/index.html', context)


def products(request: HttpRequest):
    context = {
        "title": "Store - Каталог",
        "categories": ProductCategory.objects.all(),
        "products": Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

