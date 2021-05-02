from django.shortcuts import render
from store.models import Product
from category.models import Category


def home(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()
    recomended_products = Product.objects.all().filter(is_recomended=True)
    new_arrivals = Product.objects.all().filter(is_new_arrival=True)

    context = {
        "products": products,
        "categories": categories,
        'new_arrivals' : new_arrivals,
        'recomended_products':recomended_products,

    }
    return render(request, "home.html", context)


def aboutus(request):
    return render(request,"others/aboutus.html")