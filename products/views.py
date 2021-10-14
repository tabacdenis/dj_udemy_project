from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from products.models import ProductCategory, Product, Basket


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


@login_required
def basket_add(request: HttpRequest, product_id: int):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required
def basket_delete(request, product_id):
    basket = Basket.objects.get(id=product_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
