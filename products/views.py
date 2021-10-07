from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    context = {
        "title": "Store"
    }
    return render(request, 'products/index.html', context)


def products(request: HttpRequest):
    context = {
        "title": "Store - Каталог"
    }
    return render(request, 'products/products.html', context)


def test_context(request: HttpRequest):
    context = {
        "title": "Test",
        "header": "Test Header",
        "username": "Test Username",
        "products": [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        "products_of_promotions": [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ]
    }
    return render(request, 'products/test_context.html', context)
